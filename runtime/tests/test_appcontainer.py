import http.server
import json
import os
from pathlib import Path
import socketserver
import subprocess
import sys
import tempfile
import threading
import time
import unittest
import urllib.request

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from runtime.appcontainer import run_staged


@unittest.skipUnless(os.name=='nt', 'native Windows integration')
class AppContainerTests(unittest.TestCase):
    def test_workspace_outside_reads_writes_network_and_worker_separation(self):
        with tempfile.TemporaryDirectory() as directory:
            parent=Path(directory)
            (parent/'canary.txt').write_text('outside synthetic canary')
            class Handler(http.server.BaseHTTPRequestHandler):
                def do_GET(self):
                    self.send_response(200); self.end_headers(); self.wfile.write(b'network-canary')
                def log_message(self,*args): pass
            with socketserver.TCPServer(('127.0.0.1',0),Handler) as server:
                thread=threading.Thread(target=server.serve_forever,daemon=True); thread.start()
                try:
                    url=f'http://127.0.0.1:{server.server_address[1]}/'
                    self.assertEqual(urllib.request.urlopen(url,timeout=3).read(),b'network-canary')
                    host=subprocess.run([r'C:\Windows\System32\curl.exe','--noproxy','*','--max-time','2',url],capture_output=True,text=True)
                    self.assertEqual(host.returncode,0)
                    self.assertIn('network-canary',host.stdout)
                    script='\n'.join(['@echo off','echo local-ok>local.txt',
                        'type local.txt>local-read.txt',
                        r'type ..\canary.txt>outside-read.txt 2>outside-read-error.txt',
                        'echo %errorlevel%>read-code.txt',r'echo denied>..\forbidden.txt 2>outside-write-error.txt',
                        'echo %errorlevel%>write-code.txt',
                        f'curl.exe --noproxy * --max-time 2 {url}>network.txt 2>network-error.txt',
                        'echo %errorlevel%>network-code.txt'])
                    result=run_staged(parent, {'test.cmd':script},[r'C:\Windows\System32\cmd.exe','/d','/c','test.cmd'])
                    workspace=Path(result['workspace'])
                    self.assertEqual(result['exit_code'],0)
                    self.assertIn('local-ok',(workspace/'local-read.txt').read_text())
                    self.assertNotEqual((workspace/'read-code.txt').read_text().strip(),'0')
                    self.assertIn('Access is denied',(workspace/'outside-read-error.txt').read_text())
                    self.assertFalse((parent/'forbidden.txt').exists())
                    self.assertNotEqual((workspace/'network-code.txt').read_text().strip(),'0')
                    # Windows filtering can reject immediately or silently drop.
                    self.assertIn(int((workspace/'network-code.txt').read_text().strip()),(7,28))
                    self.assertEqual(urllib.request.urlopen(url,timeout=3).read(),b'network-canary')
                    self.assertNotIn('network-canary',(workspace/'network.txt').read_text())
                    second=run_staged(parent,{'test.cmd':f'@echo off\ntype "{workspace / "local.txt"}">read.txt 2>error.txt\n'},
                                      [r'C:\Windows\System32\cmd.exe','/d','/c','test.cmd'])
                    self.assertIn('Access is denied',(Path(second['workspace'])/'error.txt').read_text())
                finally:
                    server.shutdown(); thread.join()

    def test_timeout_stops_descendant_writes(self):
        with tempfile.TemporaryDirectory() as directory:
            result=run_staged(directory, {
                'parent.cmd':'@echo off\nstart "" /b cmd.exe /d /c child.cmd\n:wait\ngoto wait\n',
                'child.cmd':'@echo off\n:loop\necho tick>>heartbeat.txt\ngoto loop\n'},
                [r'C:\Windows\System32\cmd.exe','/d','/c','parent.cmd'],timeout=.3)
            self.assertEqual(result['status'],'timeout')
            heartbeat=Path(result['workspace'])/'heartbeat.txt'
            before=heartbeat.read_bytes()
            self.assertTrue(before)
            time.sleep(.2)
            self.assertEqual(before,heartbeat.read_bytes())

    def test_revocation_stops_a_running_worker(self):
        with tempfile.TemporaryDirectory() as directory:
            started=time.monotonic()
            result=run_staged(directory, {'loop.cmd':'@echo off\n:loop\ngoto loop\n'},
                [r'C:\Windows\System32\cmd.exe','/d','/c','loop.cmd'],timeout=5,
                alive=lambda:time.monotonic()-started<1)
            self.assertEqual(result['status'],'revoked')
