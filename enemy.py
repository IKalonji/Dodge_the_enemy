import turtle
from random import randint

enemy = turtle.Turtle()
enemy.left(270)
enemy.penup()
enemy.goto(0,245)

def enemy_movement():
    '''Function to move the enemy randomly'''
    enemy.speed(1)
    x, y = randint(-199,199), randint(-299,245)
    enemy.goto(x,y)


    