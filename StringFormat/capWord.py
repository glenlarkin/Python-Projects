#!python3
# Capitalizes the first letter of each word given to it
import pyperclip

context = input('Enter any words you would like to Capitalize\n')

result = context.title()
pyperclip.copy(result)
print(result)