import os
import subprocess
from colors import colors

# check file state, to see if it's already obfuscated
def file_obfuscated(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as opened_file:
            file_content = opened_file.read()
            if "pyarmor" in file_content:
                return True
        return False
    except:
        print(colors.RED + f"Error reading file {file_path}" + colors.END)

# resolve pyarmor license folder size limitation
def resolver(folder_path):
    for dir_name in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, dir_name)):
            # ignore genereated pyarmor folders
            if "pyarmor" in dir_name:
                continue

            # recursively call resolver to obfuscate each file in nested folders
            resolver(f"{folder_path}\{dir_name}")
        else:
            if file_obfuscated(f"{folder_path}\{dir_name}"):
                continue
        
            command = f"pyarmor gen -O . -i --enable-jit {dir_name}"

            try:
                result = subprocess.run(command, cwd=folder_path, shell=True)
                result.check_returncode()
                print(colors.GREEN + f"Obfuscated {dir_name} successfully" + colors.END)
            except subprocess.CalledProcessError as e:
                print(colors.RED + f"Error obfuscating {dir_name}: {e}" + colors.END)

def obfuscate(project_path):
    for dir_name in os.listdir(project_path):
        # ignore hidden
        if dir_name.startswith("."):
            continue
        
        command = f"pyarmor gen -O . -r -i --enable-jit {dir_name}"
        
        try:
            result = subprocess.run(command, cwd=project_path, shell=True)
            result.check_returncode()
            print(colors.GREEN + f"Obfuscated {dir_name} successfully" + colors.END)
        except subprocess.CalledProcessError as e:
            print(colors.RED + f"Error obfuscating {dir_name}: {e}" + colors.END)

            if os.path.isdir(os.path.join(project_path, dir_name)):
                print(colors.YELLOW + "Folder detected!, applying double recursive obfuscating to resolve issue" + colors.END)
                resolver(f"{project_path}\{dir_name}")
