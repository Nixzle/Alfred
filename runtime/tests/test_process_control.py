import sys
import tempfile
import time
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from process_control import run_process


class ProcessControlTests(unittest.TestCase):
    def test_timeout_terminates_descendant(self):
        with tempfile.TemporaryDirectory() as folder:
            marker=Path(folder)/'escaped.txt'
            child="import time,pathlib; time.sleep(1); pathlib.Path("+repr(str(marker))+").write_text('escaped')"
            parent="import subprocess,sys,time; subprocess.Popen([sys.executable,'-c',"+repr(child)+"]); time.sleep(10)"
            result=run_process([sys.executable,'-c',parent],folder,0.4)
            self.assertEqual(result['status'],'timeout')
            time.sleep(1.1)
            self.assertFalse(marker.exists())

    def test_exit_and_revocation(self):
        with tempfile.TemporaryDirectory() as folder:
            result=run_process([sys.executable,'-c','raise SystemExit(7)'],folder,5)
            self.assertEqual(result['exit_code'],7)
            result=run_process([sys.executable,'-c','import time; time.sleep(10)'],folder,5,alive=lambda:False)
            self.assertEqual(result['status'],'revoked')
