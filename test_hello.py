
import unittest
import subprocess

class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        process = subprocess.run(['python3', '/workspace/hello.py'], capture_output=True, text=True)
        self.assertEqual(process.stdout.strip(), "Hello World")

if __name__ == '__main__':
    unittest.main()
