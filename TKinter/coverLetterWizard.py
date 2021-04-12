#!usr/bin/python3
import tkinter as tk
from docxtpl import DocxTemplate
import datetime
from pathlib import Path


def modifyDoc(companyName, positionName):
    todayDate = datetime.datetime.today().strftime('%m/%d/%Y')

        # Assigns each variable a dictionary value of the same name
    contextDict = { 'todayDate': todayDate, 'companyName': companyName, 'postionName': positionName}

        # Open Master CoverLetter template  
    doc = DocxTemplate("CoverLetter/mainCoverLetter.docx")

        # Load Variable names into file and replace template
    doc.render(contextDict)

        # Save the file with Modified filename
    doc.save(companyName + '_' + positionName + '_CoverLetter.docx')
    
    exportPath = Path.cwd()
    label['text'] = 'Success!\nYour Cover Letter has been created\nIt has been placed in: ' + str(exportPath)

root = tk.Tk()
root.geometry("600x500")
root.title('Cover Letter Wizard')

backgroundImage = tk.PhotoImage(file='CoverLetter/landscape.png')
backgroundLabel = tk.Label(root, image=backgroundImage)
backgroundLabel.place(relheight=1, relwidth=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.74, relheight=0.2, anchor='n')

companyLabel = tk.Label(frame, text='Company Name:')
companyLabel.place(relheight=0.2, relwidth=0.3)

postionLabel = tk.Label(frame, text='Postion:')
postionLabel.place(relx=0.3, relheight=0.2, relwidth=0.3)

companyEntry = tk.Entry(frame, justify='center')
companyEntry.place(rely=0.25, relwidth=0.3, relheight=0.6)

positionEntry = tk.Entry(frame, justify='center')
positionEntry.place(relx=0.3, rely=0.25, relwidth=0.3, relheight=0.6)

button = tk.Button(frame, text="Create Cover Letter", font=40, command=lambda: modifyDoc(companyEntry.get(), positionEntry.get()))
button.place(relx=0.6,  relheight=0.8, relwidth=0.4)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()