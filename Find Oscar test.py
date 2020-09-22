#! python3
#Find Oscar Test.py - finds the name Oscar, in any case within a sentence

import re
def oscarFinder(oscar):                 #Accepts String from user to find oscar in
    text = re.compile(r'oscar', re.I)   #re.I makes it find any case.
    print(text.search(oscar))           #Takes text that user needs to find oscar in

print(oscarFinder('Where is my Oscar? I cant seem to find him'))