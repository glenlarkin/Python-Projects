import zipfile, os
from pathlib import Path

p = Path.home()

exampleZip = zipfile.ZipFile(p / 'example.zip')
exampleZip.extractall() #Can be used to place zip in existing or new file
exampleZip.close()
