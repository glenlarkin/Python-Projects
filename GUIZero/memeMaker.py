# Imports ---------------
from guizero import App, TextBox, Drawing, Combo, Slider

# Functions -------------
def draw_meme():
    meme.clear()
    meme.image(0, 0, "GUIZero/Pizza.png")
    
    meme.text(
        20, 20, top_text.value,
        color=color.value,
        size=size.value,
        font=font_type.value)
    meme.text(
        20, 320, bottom_text.value,
        color=color.value,
        size=size.value,
        font=font_type.value,
        )

# App -------------------
app = App("Meme Generator")


# Widgets ---------------
top_text = TextBox(app, "top text", command=draw_meme)
bottom_text = TextBox(app, "bottom text", command=draw_meme)

color = Combo(app,
    options=['black','white','red','green','blue','orange'], 
    command=draw_meme,
    selected='blue')

font_type = Combo(app,
    options=['times new roman','verdana','courier','impact'],
    command=draw_meme,
    selected='verdana')

size = Slider(app, start=20, end=40, command=draw_meme)

meme = Drawing(app, width='fill', height='fill')


# Display ---------------
draw_meme()
app.display()