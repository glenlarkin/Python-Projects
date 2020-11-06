from pathlib import Path
import os

os.makedirs('C:\\delicious\\walnut\\waffles')   #Makes 3 folders nested inside each other

p = Path('C:/Users/Glenl/spam.txt')

print(p.anchor) #Shows letter assigned to drive

p.parent   # This is a path object, not a string.

p.name      # File name.extension

p.stem      # Only Name of file

p.suffix    # .Extension of file

p.drive     # Shows letter assigned to drive file is on

os.path.dirname(p)      # Finds path of folder that file resides in

os.path.basename(p)     # Finds Name of File and extension

os.path.getsize('C:\\Windows\\System32\\calc.exe')      # Gets total size (in Kb) of a file

totalSize = 0
for filename in os.listdir('C:\\Windows\\System32'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Windows\\System32', filename))
print(totalSize)

p = Path('C:/Users/Glenl/Desktop')
p.glob('*')
list(p.glob('*'))  # Make a list from the generator.
list(p.glob('*.txt')) # Lists all text files
list(p.glob('project?.docx'))   # Question mark (?) stands for any single character
list(p.glob('*.?x?'))    #Finds .exe files and txt files. anything with an X in the middle

p = Path('C:/Users/Al/Desktop')
for textFilePathObj in p.glob('*.txt'):
    print(textFilePathObj) # Prints the Path object as a string.

winDir = Path('C:/Windows')
winDir.exists() # Checks if path is valid
winDir.is_dir() # Checks if path is a folder
winDir.is_file()    # Checks if item is an individual file

dDrive = Path('D:/')
if dDrive.exists() == False:
    print('Oops! It looks like I forgot to plug in my flash drive.')

p = Path('spam.txt')    # Sets path to a file named spam.txt
p.write_text('Hello, world!')   # Writes a string in file
p.read_text()           # reads string from file