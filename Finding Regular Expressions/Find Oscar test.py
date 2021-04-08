#! python3
#Find Oscar Test.py - finds the name Oscar, in any case within a sentence

import re
def oscarFinder(oscar):                 #Accepts String from user to find oscar in
    text = re.compile(r'oscar', re.I)   #re.I helps us find any case.
            
    return text.findall(oscar)
    
userInput = input('Input text about Oscar\n') #Allows the user to input text about Oscar
result = oscarFinder(userInput)               #Displays the match within the text
print(result)