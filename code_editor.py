import subprocess

def run_code(code):
    try:
        process = subprocess.run(['python3', '-c', code], capture_output=True, text=True)
        return process.stdout, process.stderr
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")