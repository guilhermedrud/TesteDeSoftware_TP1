import unittest
import subprocess
from tempfile import SpooledTemporaryFile as tempfile

class TestDraw(unittest.TestCase):
        def test_draw(self):
                f = tempfile()
                f.write(b'a2 a4\nb8 c6\ne2 e3\nc6 d4\ndraw\ndraw\n')
                f.seek(0)
                
                cp = subprocess.run(["python3","main.py"], stdin=f, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                
                f.close()
                
                self.assertIn('Draw!', cp.stdout)

if __name__ == '__name__':
    unittest.main()
