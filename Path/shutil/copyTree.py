import shutil, os
from pathlib import Path


p = Path.cwd()

#Creates newFolder directory and placed contents of copyFolder in it
shutil.copytree(p / 'copyFolder', p / 'newFolder')