'''DODGE THE ENEMY GUI GAME WHERE THE USER NEEDS TO REACH 
THE TOP OF THE SCREEN WITHOUT BEING IN CONTACT WITH THE ENEMY'''

import turtle
import enemy
import player
import setup
import threading
# from multiprocessing import Process






def move_player():
    '''Function to move player'''

    turtle.listen()
    turtle.onkey(player.up, 'Up')
    turtle.onkey(player.down, 'Down')
    turtle.onkey(player.left, 'Left')
    turtle.onkey(player.right, 'Right')

if __name__ == "__main__":
    
    setup.border()
    
    while True:
        enemy.enemy_movement()
        move_player()
    # process_1 = Process(target=move_player)
    # process_1.start()
    # process_2 = Process(target=enemy.enemy_movement)
    # process_2.start()

    turtle.mainloop()
