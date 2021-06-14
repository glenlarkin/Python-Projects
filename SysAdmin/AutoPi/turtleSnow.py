#!/bin/python3

import turtle, random
snowy = turtle.Turtle()

turtle.Screen().bgcolor("grey")
colors = ["cyan", "purple", "white", "blue"]

snowy.penup()
snowy.forward(90)
snowy.left(45)
snowy.pendown()


def branch():
    for i in range(3):
        for i in range(3):
            snowy.forward(30)
            snowy.backward(30)
            snowy.right(45)
        snowy.left(90)
        snowy.backward(30)
        snowy.left(45)
    snowy.right(90)
    snowy.forward(90)
    snowy.color(random.choice(colors))


for i in range(8):
    branch()
    snowy.left(45)


