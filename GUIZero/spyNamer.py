# Imports ---------------

from guizero import App, Text, PushButton
from random import choice

# Functions -------------

def choose_name():
    first_names = ['David', 'Steven', 'Pamala', 'Suzy', 'Albert', 'Joel', 'Thomas', 'Marie', 'Jennie', ]
    last_names = ['Stevenson', 'Hackenbush', 'WonderFred', 'TotallyARealName', 'Not Suspicious', 'Fuck', 'Dixon', 'Packer', 'Jobs']
    spy_name = choice(first_names) + ' ' + choice(last_names)
    name.value = spy_name
    
# App -------------------

app = App("TOP SECRET: DON'T BLAB")

# Widgets ---------------

title = Text(app, "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text= 'Your Destiny')
button.bg = 'red'
button.text_size = 20
name = Text(app, text='')

# Display ---------------

app.display()