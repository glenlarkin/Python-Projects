import zipfile
from pathlib import Path

p = Path.home()

exampleZip = zipfile.ZipFile(p / 'Automate_the_Boring_Stuff_2e_onlinematerials.zip')
exampleZip.extractall() #Can be used to place zip in existing or new file
exampleZip.close()
