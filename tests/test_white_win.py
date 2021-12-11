import unittest
import subprocess
from tempfile import SpooledTemporaryFile as tempfile

class TestWhiteWin(unittest.TestCase):
        def test_white_win(self):
                f = tempfile()
                f.write(b'g2 g3\nh7 h6\nf1 g2\ng7 g5\ng2 f3\nf7 f6\nf3 h5\nf8 g7\nh5 e8\n')
                f.seek(0)
                
                cp = subprocess.run(["python3","main.py"], stdin=f, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                f.close()
                
                self.assertIn('White win!', cp.stdout)

if __name__ == '__name__':
    unittest.main()
