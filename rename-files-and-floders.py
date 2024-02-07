# %%
import os
from pathlib import Path

folder = input("Enter folder: ")
l = os.listdir(folder)

our_files = Path(folder)
print(our_files.is_dir())

# %%
replace_text = input("Replace text: ")
with_text = input("With text: ")

# Rename files in directory
for filetuple in enumerate(os.listdir(folder)):
    # foldername/filename, if .py file is outside folder
    _, filename = filetuple

    src = f"{folder}\{filename}"

    new_filename = str(filename).replace(replace_text, with_text)

    dst = f"{folder}\{new_filename}"

    if src != dst:
        print(f'Existing file name: {src}')
        print(f'Updated file name: {dst}')

    # rename() function will
    # rename all the files
    os.rename(src, dst)

# %%
# Remove folder recursively
# shutil.rmtree(f'{folder}check_folder')
