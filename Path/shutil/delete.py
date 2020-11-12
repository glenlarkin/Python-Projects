import os
import shutil
from pathlib import Path

path = Path('/users/sketchmaster/documents/github/python-projects/path/copyBackup')

# Deletes one file at the path specified
os.unlink(path)

# Deletes empty folder at path
os.rmdir(path)

# Deletes folder and all files inside it
shutil.rmtree(path)

for fileName in Path.home().glob('*.rxt'):
    # os.unlink(filename)
    print(path)