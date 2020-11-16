'''Turtle screen setup'''

import turtle

turtle.screensize(200,300)
turtle.penup()
turtle.ht()

def border():

    '''Function to draw the outer border'''

    turtle.goto(-200, 250)
    turtle.pendown()
    turtle.goto(-200, -300)
    turtle.goto(200, -300)
    turtle.goto(200, 250)
    turtle.goto(-200, 250)
    turtle.penup()
