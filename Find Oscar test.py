import re
def oscarFinder():
    text = re.compile(r'oscar', re.I)
    print(text.search('Where the fuck is Oscar? maybe hes hidden in this text'))

print(oscarFinder())