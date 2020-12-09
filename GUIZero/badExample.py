from guizero import App, PushButton, Text, Combo
from string import ascii_letters

def flashText():
    if title.visible:
        title.hide()
    else:
        title.show()

def are_you_sure():
    if app.yesno("Confirmation", "Are you sure?"):
        app.info("Thanks", "Button pressed")
    else:
        app.error("Ok", "Cancelling")
app = App(title="pointless pop-ups")
app.bg = 'dark green'
button = PushButton(app, command=are_you_sure)
title = Text(app, 'Dont have a seizure pls')
a_letter = Combo(app, options=" " + ascii_letters, align="left")
b_letter = Combo(app, options=" " + ascii_letters, align="left")
c_letter = Combo(app, options=" " + ascii_letters, align="left")

app.info("Application started", "Well done you started the application")

app.repeat(1000, flashText)

app.display()