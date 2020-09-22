#! python3
#Find Oscar Test.py - finds the name Oscar, in any case within a sentence

import re
def oscarFinder():              #need to make modular pls, accept string
    text = re.compile(r'oscar', re.I)   #re.I makes it find any case
    print(text.search('Where the fuck is Oscar? maybe hes hidden in this text'))

print(oscarFinder())