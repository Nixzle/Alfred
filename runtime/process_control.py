"""Bound trusted adapter processes with timeout and descendant cleanup.

This controls lifecycle only. Callers must separately verify OS containment before
running untrusted code. A gate prevents work starting before Windows Job assignment.
"""
import ctypes
from ctypes import wintypes
import json
import os
import signal
import subprocess
import sys
import time


class WindowsJob:
    def __init__(self):
        class Basic(ctypes.Structure):
            _fields_=[('process_time',ctypes.c_int64),('job_time',ctypes.c_int64),
                      ('flags',wintypes.DWORD),('minimum',ctypes.c_size_t),('maximum',ctypes.c_size_t),
                      ('active_limit',wintypes.DWORD),('affinity',ctypes.c_size_t),
                      ('priority',wintypes.DWORD),('scheduling',wintypes.DWORD)]
        class IO(ctypes.Structure):
            _fields_=[(name,ctypes.c_uint64) for name in ('read_ops','write_ops','other_ops','read_bytes','write_bytes','other_bytes')]
        class Extended(ctypes.Structure):
            _fields_=[('basic',Basic),('io',IO),('process_memory',ctypes.c_size_t),
                      ('job_memory',ctypes.c_size_t),('peak_process',ctypes.c_size_t),('peak_job',ctypes.c_size_t)]
        self.kernel=ctypes.WinDLL('kernel32',use_last_error=True)
        self.kernel.CreateJobObjectW.argtypes=[ctypes.c_void_p,wintypes.LPCWSTR]
        self.kernel.CreateJobObjectW.restype=wintypes.HANDLE
        self.kernel.SetInformationJobObject.argtypes=[wintypes.HANDLE,ctypes.c_int,ctypes.c_void_p,wintypes.DWORD]
        self.kernel.AssignProcessToJobObject.argtypes=[wintypes.HANDLE,wintypes.HANDLE]
        self.kernel.CloseHandle.argtypes=[wintypes.HANDLE]
        self.handle=self.kernel.CreateJobObjectW(None,None)
        if not self.handle: raise ctypes.WinError(ctypes.get_last_error())
        limits=Extended(); limits.basic.flags=0x2000  # KILL_ON_JOB_CLOSE
        if not self.kernel.SetInformationJobObject(self.handle,9,ctypes.byref(limits),ctypes.sizeof(limits)):
            self.close(); raise ctypes.WinError(ctypes.get_last_error())

    def assign(self,process):
        if not self.kernel.AssignProcessToJobObject(self.handle,wintypes.HANDLE(int(process._handle))):
            raise ctypes.WinError(ctypes.get_last_error())

    def close(self):
        if self.handle:
            self.kernel.CloseHandle(self.handle); self.handle=None


def run_process(command, cwd, timeout, env=None, alive=lambda:True):
    if not 0 < timeout <= 3600:
        raise ValueError('process timeout must be bounded')
    if not alive():
        return {'status':'revoked','exit_code':None,'elapsed_ms':0}
    # No inherited provider credentials. Adapter-specific additions require the
    # trusted supervisor to pass an explicit environment.
    environment = {k:v for k,v in os.environ.items() if k.upper() in
                   {'SYSTEMROOT','WINDIR','COMSPEC','PATH','TEMP','TMP'}} if env is None else env
    gate="import sys,json,subprocess; command=json.loads(sys.stdin.readline()); raise SystemExit(subprocess.call(command))"
    job=WindowsJob() if os.name=='nt' else None
    process=None
    started=time.monotonic()
    try:
        process=subprocess.Popen([sys.executable,'-I','-c',gate],cwd=cwd,env=environment,
            stdin=subprocess.PIPE,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0,
            start_new_session=os.name!='nt')
        if job: job.assign(process)
        if not alive():
            return {'status':'revoked','exit_code':None,'elapsed_ms':round((time.monotonic()-started)*1000)}
        process.stdin.write((json.dumps(command)+'\n').encode()); process.stdin.flush(); process.stdin.close()
        status='finished'
        while process.poll() is None:
            if not alive(): status='revoked'; break
            if time.monotonic()-started >= timeout: status='timeout'; break
            time.sleep(0.05)
        return {'status':status,'exit_code':process.poll(), 'elapsed_ms':round((time.monotonic()-started)*1000)}
    finally:
        if job: job.close()
        if process:
            if os.name!='nt':
                try: os.killpg(process.pid,signal.SIGKILL)
                except ProcessLookupError: pass
            elif process.poll() is None:
                process.kill()
            process.wait(timeout=5)
            if process.stdin and not process.stdin.closed: process.stdin.close()
