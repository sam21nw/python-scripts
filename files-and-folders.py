# %%
from datetime import datetime
from pathlib import Path
import os

while True:
    folder = input("Input a Folder: ")
    if Path(folder).is_dir() == False:
        print(f"Input a valid Folder")
    if Path(folder).is_dir() == True and not "".__eq__(folder):
        print(f"Input folder is '{folder}'")
        our_folder = Path(folder)
        break


# %%
if not our_folder.is_dir():
    print("Not a folder..")
else:
    replace_text = input("Replace text: ")
    with_text = input("With text: ")

    for file in our_folder.iterdir():

        dir = file.parent

        f = Path(file)
        old_name, ext = f.stem, f.suffix
        new_name = f"{old_name.replace(replace_text, with_text)}{ext}"

        file.rename(Path(dir, new_name))
