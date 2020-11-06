#! python3
# CLModifier.py - Modify a Template Cover Letter to match the qualifications needed for a job.

from docxtpl import DocxTemplate
import datetime
from pathlib import Path

companyName = input('Which Company are you applying to?\n')
positionName = input('What Position are they filling?\n')

todayDate = datetime.datetime.today().strftime('%m/%d/%Y')

# Assigns each variable a dictionary value of the same name
contextDict = { 'todayDate': todayDate, 'companyName': companyName, 'postionName': positionName}

# Open Master CoverLetter template
doc = DocxTemplate("masterCoverLetter.docx")

# Load Variable names into file and replace template
doc.render(contextDict)

# Save the file with Modified filename
doc.save(companyName + '_' + positionName + '_CoverLetter.docx')

path = Path.cwd()
print('Success!\nYour Cover Letter has been created and has been placed in: ' + str(path))
