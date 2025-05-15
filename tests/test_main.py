import subprocess

def test_main():
    process = subprocess.run(['python', 'src/main.py'], capture_output=True, text=True, cwd='/workspace')
    assert process.returncode == 0
    assert process.stdout == "Hello World!!\n"
