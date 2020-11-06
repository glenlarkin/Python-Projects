#! python3
# coverLetter.py - Modify a master cover letter template to match the qualifications needed for a job.

from docxtpl import DocxTemplate
import datetime

companyName = input('Which Company are you applying to?\n')
positionName = input('What Position are they filling?\n')

todayDate = datetime.datetime.today().strftime('%m/%d/%Y')

# Assigns each variable a dictionary value of the same name
contextDict = { 'todayDate': todayDate, 'companyName': companyName, 'postionName': positionName}

# Open Master CoverLetter template
doc = DocxTemplate("master_cover_letter.docx")

# Load Variable names into file and replace template
doc.render(contextDict)

# Save the file with Modified filename
doc.save('Cover_Letter_' + companyName + '_' + positionName + '.docx')