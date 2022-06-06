# %%
from datetime import datetime
from pathlib import Path
import os

folder = input("Enter folder: ")
our_folder = Path(folder)

if not our_folder.is_dir():
    print(f"{our_folder} is not a folder..")
else:
    print(f"{our_folder} is selected")

# %%
if not our_folder.is_dir():
    print("Not a folder..")
else:
    for file in our_folder.iterdir():

        dir = file.parent

        f = Path(file)
        old_name, ext = f.stem, f.suffix
        new_name = f"{old_name.replace('sample', 'test')}{ext}"

        file.rename(Path(dir, new_name))

# %%
