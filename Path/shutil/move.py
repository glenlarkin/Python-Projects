import shutil

#moves spam.txt to a newfolder
shutil.move('C:\\spam.txt', 'C:\\newFolder')

shutil.move('C:\\spam.txt', "C:\\eggs\\new_spam.txt")

shutil.move('C:\\spam.txt', 'C:\\eggs')