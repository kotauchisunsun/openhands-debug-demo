
import subprocess

def test_hello_world():
    process = subprocess.run(['python3', '/workspace/main.py'], capture_output=True, text=True)
    assert process.returncode == 0
    assert process.stdout == "Hello World!\n"
