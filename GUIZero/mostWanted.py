#!python
# Creates a most wanted poster for pizza

from guizero import App, Text, Picture

app = App('Wanted!')
app.bg = (251, 251, 208)

wanted_text = Text(app, 'WANTED')
wanted_text.text_size = 50
wanted_text.font = 'Times New Roman'

pizza = Picture(app, image='Pizza.png')

reward_text = Text(app, 'Reward if found!')

app.display()