import requests
import re

# get the data
data = requests.get('https://research.utah.edu/about/staff.php')

# extract the phone numbers, emails, whatever
phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

alpha_emails = sorted(emails)
for e in alpha_emails:
    print(e)