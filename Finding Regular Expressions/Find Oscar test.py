#! python3
#Find Oscar Test.py - finds the name Oscar, in any case within a sentence

import re
def oscarFinder(oscar):                 #Accepts String from user to find oscar in
    text = re.compile(r'oscar', re.I)   #re.I helps us find any case.
    print(text.findall(oscar))          #Takes text that user needs to find oscar in
    
userInput = input('Input text about Oscar\n') #Allows the user to input text about Oscar
print(oscarFinder(userInput))                 #Displays the match within the text