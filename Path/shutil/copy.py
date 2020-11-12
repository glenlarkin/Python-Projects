import shutil
import os
from pathlib import Path

p = Path.cwd()

#Takes contents of spam.txt and copies them to copyFolder directory
shutil.copy(p / 'spam.txt', p / 'copyFolder')

#Takes contents of spam.txt and copies them to copyBackup Directory
shutil.copy(p / 'spam.txt', p / 'copyBackup')