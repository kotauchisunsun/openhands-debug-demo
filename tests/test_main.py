
import unittest
import subprocess

class TestMain(unittest.TestCase):
    def test_output(self):
        process = subprocess.run(['python', '/workspace/src/main.py'], capture_output=True, text=True)
        self.assertEqual(process.stdout.strip(), "Hello World!!")

if __name__ == '__main__':
    unittest.main()
