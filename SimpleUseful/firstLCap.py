#!python3
# Capitalizes the first letter of each word given to it
from tkinter import Tk

context = input('Enter any words you would like to Capitalize\n')

result = context.title()
print(result)

r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(result)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()