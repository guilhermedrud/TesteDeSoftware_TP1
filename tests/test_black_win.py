import unittest
import subprocess
from tempfile import SpooledTemporaryFile as tempfile

class TestBlackWin(unittest.TestCase):
        def test_black_win(self):
                f = tempfile()
                f.write(b'a2 a4\nb8 c6\ne2 e3\nc6 d4\ne1 e2\nd4 e2\n')
                f.seek(0)
                
                cp = subprocess.run(["python3","main.py"], stdin=f, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                f.close()
                
                self.assertIn('Black win!', cp.stdout)
                
                cp.kill()

if __name__ == '__name__':
    unittest.main()
