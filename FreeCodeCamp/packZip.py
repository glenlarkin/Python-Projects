#!python3
#Packing and unpacking zips

student = ['john', 'sam', 'steve', 'bob']

grade = [6,7,7,8]


#creates list into a zip file
classes = list(zip(student,grade))

#unpack the zip file
new_students, grades = zip(*classes)