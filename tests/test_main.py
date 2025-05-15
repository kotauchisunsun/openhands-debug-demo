import subprocess

def test_main():
    process = subprocess.run(['python', '/workspace/src/main.py'], capture_output=True, text=True)
    assert process.returncode == 0
    assert process.stdout == "Hello World!!\n"
