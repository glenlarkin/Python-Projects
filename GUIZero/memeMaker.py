from guizero import App, TextBox, Drawing

app = App("meme")
top_text = TextBox(app, "top text")
bottom_text = TextBox(app, "bottom text")
app.display()