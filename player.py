'''Main player module'''

import turtle

issa = turtle.Turtle()
issa.color("green")
issa.left(90)
issa.penup()
issa.goto(0,-290)


'''Player movement'''

def up():
    '''Function to move issa up'''
    issa.speed(10)
    x = issa.xcor()
    y = issa.ycor()
    issa.goto(x,y+5)

def down():
    '''Function to move issa down'''
    issa.speed(10)
    x = issa.xcor()
    y = issa.ycor()
    issa.goto(x,y-5)
    pass

def left():
    '''Function to move issa left'''
    issa.speed(10)
    x = issa.xcor()
    y = issa.ycor()
    issa.goto(x-5,y)
    pass

def right():
    '''Function to move issa right'''
    issa.speed(10)
    x = issa.xcor()
    y = issa.ycor()
    issa.goto(x+5,y)
    pass

