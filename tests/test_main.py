import subprocess

def test_main():
    process = subprocess.run(['python', 'src/main.py'], capture_output=True, text=True, check=True)
    assert process.stdout.strip() == "Hello World!!"
