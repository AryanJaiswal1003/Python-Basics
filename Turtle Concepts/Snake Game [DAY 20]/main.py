import time #Time Module
from turtle import Screen
from snake import Snakes

#Setting up the Screen Configurations.
screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor('black')
screen.title(titlestring="My Snake Game")
screen.tracer(n=0)

"""The screen.tracer() --> manages frequency of screen updates for during animations. By default, screen updates after 
    each turtle movt, but with tracer(n) --> you can limit updates to occur every n movt's. 
        Setting tracer(0) --> completely stops automatic updates, & allows manual refresh screen with screen.update()"""

snake = Snakes()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()  ##screen.tracer()
    time.sleep(0.1)  # --> pauses program's execution for specified number of seconds, allowing delays/timed actions.

    snake.move()




screen.exitonclick()