"""Windows offline staging worker using native AppContainer and a kill-on-close job.

Only fresh staging directories are supported. Do not point this at a user's checkout.
No network capability or loopback exemption is granted. System resources available
to ordinary AppContainers remain available; this is not a VM or a universal deny-all.
"""
import ctypes as C
from ctypes import wintypes as W
import os
from pathlib import Path
import subprocess
import time
import uuid

from .process_control import WindowsJob


def run_staged(staging_parent, files, command, timeout=10, alive=lambda:True):
    if os.name != 'nt':
        raise RuntimeError('Windows required')
    if not 0 < timeout <= 300 or not command:
        raise ValueError('bounded command required')
    if not alive():
        raise PermissionError('worker authority is no longer active')
    if not isinstance(files,dict) or len(files)>50:
        raise ValueError('at most 50 staged text files are accepted')
    for name, content in files.items():
        if (not isinstance(name,str) or Path(name).name!=name or ':' in name or
                name in {'.','..'} or name.rstrip(' .')!=name or not isinstance(content,str)):
            raise ValueError('only plain staged text file names are accepted')
        if (name.upper().split('.')[0] in {'CON','PRN','AUX','NUL',*[f'COM{i}' for i in range(1,10)],*[f'LPT{i}' for i in range(1,10)]}
                or len(content.encode('utf-8'))>1048576):
            raise ValueError('reserved filename or oversized staged file')
    parent = Path(staging_parent).resolve(strict=True)
    workspace = parent / ('worker-'+uuid.uuid4().hex)
    workspace.mkdir()
    for name, content in files.items():
        (workspace/name).write_text(content, encoding='utf-8')

    kernel = C.WinDLL('kernel32', use_last_error=True)
    userenv = C.WinDLL('userenv', use_last_error=True)
    advapi = C.WinDLL('advapi32', use_last_error=True)
    ptr = C.c_void_p
    class Startup(C.Structure):
        _fields_=[('cb',W.DWORD),('reserved',W.LPWSTR),('desktop',W.LPWSTR),('title',W.LPWSTR),
                  ('x',W.DWORD),('y',W.DWORD),('xs',W.DWORD),('ys',W.DWORD),
                  ('xc',W.DWORD),('yc',W.DWORD),('fill',W.DWORD),('flags',W.DWORD),
                  ('show',W.WORD),('reserved2size',W.WORD),('reserved2',ptr),
                  ('stdin',W.HANDLE),('stdout',W.HANDLE),('stderr',W.HANDLE)]
    class Extended(C.Structure):
        _fields_=[('startup',Startup),('attributes',ptr)]
    class Process(C.Structure):
        _fields_=[('process',W.HANDLE),('thread',W.HANDLE),('pid',W.DWORD),('tid',W.DWORD)]
    class Caps(C.Structure):
        _fields_=[('sid',ptr),('capabilities',ptr),('count',W.DWORD),('reserved',W.DWORD)]
    userenv.CreateAppContainerProfile.argtypes=[W.LPCWSTR,W.LPCWSTR,W.LPCWSTR,ptr,W.DWORD,C.POINTER(ptr)]
    userenv.CreateAppContainerProfile.restype=C.c_long
    userenv.DeleteAppContainerProfile.argtypes=[W.LPCWSTR]
    userenv.DeleteAppContainerProfile.restype=C.c_long
    advapi.ConvertSidToStringSidW.argtypes=[ptr,C.POINTER(W.LPWSTR)]
    advapi.FreeSid.argtypes=[ptr]
    kernel.LocalFree.argtypes=[ptr]
    kernel.InitializeProcThreadAttributeList.argtypes=[ptr,W.DWORD,W.DWORD,C.POINTER(C.c_size_t)]
    kernel.UpdateProcThreadAttribute.argtypes=[ptr,W.DWORD,C.c_size_t,ptr,C.c_size_t,ptr,ptr]
    kernel.DeleteProcThreadAttributeList.argtypes=[ptr]
    kernel.CreateProcessW.argtypes=[W.LPCWSTR,W.LPWSTR,ptr,ptr,W.BOOL,W.DWORD,ptr,W.LPCWSTR,C.POINTER(Extended),C.POINTER(Process)]
    kernel.ResumeThread.argtypes=[W.HANDLE]
    kernel.WaitForSingleObject.argtypes=[W.HANDLE,W.DWORD]
    kernel.GetExitCodeProcess.argtypes=[W.HANDLE,C.POINTER(W.DWORD)]
    kernel.TerminateProcess.argtypes=[W.HANDLE,W.UINT]
    kernel.CloseHandle.argtypes=[W.HANDLE]
    sid=ptr(); sid_text=W.LPWSTR(); info=Process(); attributes=None
    moniker='Sanctum.Worker.'+uuid.uuid4().hex
    job=WindowsJob(); profile=False
    def check(ok):
        if not ok: raise C.WinError(C.get_last_error())
    try:
        hr=userenv.CreateAppContainerProfile(moniker,moniker,'Ephemeral offline Sanctum worker',None,0,C.byref(sid))
        if hr < 0: raise OSError('CreateAppContainerProfile failed: '+hex(hr & 0xffffffff))
        profile=True
        check(advapi.ConvertSidToStringSidW(sid,C.byref(sid_text)))
        # Grant only the fresh staging directory to this unique package principal.
        for args in ([str(workspace),'/grant', '*'+sid_text.value+':(OI)(CI)M','/T','/Q'],
                     [str(workspace),'/setintegritylevel','(OI)(CI)L','/T','/Q']):
            subprocess.run([str(Path(os.environ['SYSTEMROOT'])/'System32'/'icacls.exe'),*args],
                           check=True,capture_output=True,creationflags=subprocess.CREATE_NO_WINDOW)
        size=C.c_size_t()
        kernel.InitializeProcThreadAttributeList(None,1,0,C.byref(size))
        attributes=C.create_string_buffer(size.value)
        check(kernel.InitializeProcThreadAttributeList(attributes,1,0,C.byref(size)))
        caps=Caps(sid,None,0,0)
        check(kernel.UpdateProcThreadAttribute(attributes,0,0x20009,C.byref(caps),C.sizeof(caps),None,None))
        startup=Extended(); startup.startup.cb=C.sizeof(startup); startup.attributes=C.cast(attributes,ptr)
        environment={'SYSTEMROOT':os.environ['SYSTEMROOT'],'WINDIR':os.environ['SYSTEMROOT'],
                     'TEMP':str(workspace),'TMP':str(workspace),'LOCALAPPDATA':str(workspace),
                     'PATH':str(Path(os.environ['SYSTEMROOT'])/'System32')}
        envblock=C.create_unicode_buffer('\0'.join(k+'='+v for k,v in sorted(environment.items()))+'\0\0')
        line=C.create_unicode_buffer(subprocess.list2cmdline(command))
        check(kernel.CreateProcessW(command[0],line,None,None,False,
                                    0x80000|0x400|0x4|0x8000000,envblock,str(workspace),C.byref(startup),C.byref(info)))
        # Process is suspended until successfully bound to its cleanup job.
        check(job.kernel.AssignProcessToJobObject(job.handle,info.process))
        if not alive():
            raise PermissionError('worker authority expired during setup')
        if kernel.ResumeThread(info.thread)==0xffffffff: raise C.WinError(C.get_last_error())
        started=time.monotonic()
        status='finished'
        while True:
            wait=kernel.WaitForSingleObject(info.process,25)
            if wait not in (0,258): raise C.WinError(C.get_last_error())
            if wait==0: break
            if not alive(): status='revoked'; break
            if time.monotonic()-started>=timeout: status='timeout'; break
        code=W.DWORD(); check(kernel.GetExitCodeProcess(info.process,C.byref(code)))
        return dict(status=status, exit_code=None if wait==258 else code.value,
                    elapsed_ms=round((time.monotonic()-started)*1000), workspace=str(workspace))
    finally:
        job.close()
        if info.process:
            # Also covers assignment failure while suspended.
            kernel.TerminateProcess(info.process,1)
            kernel.WaitForSingleObject(info.process,5000)
            kernel.CloseHandle(info.process)
        if info.thread: kernel.CloseHandle(info.thread)
        if attributes: kernel.DeleteProcThreadAttributeList(attributes)
        if profile:
            hr=userenv.DeleteAppContainerProfile(moniker)
            if hr < 0: raise OSError('AppContainer profile cleanup failed: '+hex(hr & 0xffffffff))
        if sid_text: kernel.LocalFree(C.cast(sid_text,ptr))
        if sid: advapi.FreeSid(sid)


if __name__=='__main__':
    import argparse
    import json
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--staging-parent',required=True)
    parser.add_argument('--bundle',type=Path,required=True,help='Trusted JSON object mapping simple filenames to text')
    parser.add_argument('--timeout',type=float,default=10)
    parser.add_argument('command',nargs=argparse.REMAINDER)
    args=parser.parse_args()
    command=args.command[1:] if args.command[:1]==['--'] else args.command
    result=run_staged(args.staging_parent,json.loads(args.bundle.read_text()),command,args.timeout)
    print(json.dumps(result,indent=2))
    raise SystemExit(result['exit_code'] if result['exit_code'] is not None else 1)
