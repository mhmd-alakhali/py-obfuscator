import os
import shutil
from colors import colors

def rename(file_name, path):
    firstBase, _ = os.path.splitext(file_name)
    secondBase, _ = os.path.splitext(firstBase)

    try:
        os.rename(f"{path}\{file_name}", f"{path}\{secondBase}.pyc")
        return f"{secondBase}.pyc"
    except Exception as e:
        print(colors.RED + f"Error renaming {file_name} to {secondBase}.pyc: {e}" + colors.END)
        return file_name


def format_files(folder_path):
    for dir_name in os.listdir(folder_path):
        # ignore hidden
        if dir_name.startwith("."):
            continue

        inner_path = f"{folder_path}\{dir_name}"

        if os.path.isdir(os.path.join(folder_path, dir_name)):
            if dir_name == "__pycache__":
                for file in os.listdir(inner_path):
                    # remove .cpython-39 extension
                    file_name = rename(file, inner_path)

                    try: 
                        shutil.move(f"{inner_path}\{file_name}", folder_path)
                    except Exception as e:
                        print(colors.RED + f"Error moving {file_name} file to {folder_path}: {e}" + colors.END)
                    
                try:
                    os.removedirs(inner_path)
                except Exception as e:
                    print(colors.RED + f"Error removing {inner_path} folder: {e}" + colors.END)
            else:
                format_files(inner_path)
        if dir_name.endswith(".py"):
            try:
                os.remove(inner_path)
            except Exception as e:
                print(colors.RED + f"Error removing {dir_name} file: {e}" + colors.END)