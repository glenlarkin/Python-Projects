import zipfile, os
from pathlib import Path

p = Path.home()

exampleZip = zipfile.Zipfile(p / 'example.zip')
exampleZip.namelist()
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size

print(f'Compressed file is {round(spamInfo.file_size / spamInfo.compress_size, 2)}x smaller!') 