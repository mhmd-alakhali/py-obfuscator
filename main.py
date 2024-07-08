import sys
import subprocess
from format import format_files
from obfuscate import obfuscate

def main():
    if len(sys.argv) == 2:
        project_path = sys.argv[1]

        # obfuscate code
        print("Step 1/3... \n Obfuscating")
        obfuscate(project_path)

        # compile code to pyc
        print("Step 2/3... \n Compiling code")
        subprocess.run(f"python -m compileall {project_path}", shell=True) 

        # format files -- replace .py files with .pyc
        print("Step 3/3... \n Formatting files")
        format_files(project_path)

        print("Done")

    else:
        print("Usage: python main.py <project_path>")
        sys.exit(1)

main()
