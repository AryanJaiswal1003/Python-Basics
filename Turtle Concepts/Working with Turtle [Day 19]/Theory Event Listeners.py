"""Learning More about Turtle Graphics , Event Listeners , State & Multiple Instances"""

from turtle import Turtle , Screen
tim = Turtle()
tim.shape("turtle")
screen = Screen()

def move_forwards():
    tim.forward(10)

screen.listen()

"""screen.listen() --> method in turtle module that enables program to respond to user input. Useful for interactive 
        graphics or games"""

screen.onkey(key="space" , fun=move_forwards)

"""Higher Order Function --> It operates on other functions by either taking them as arguments or returning 
    them as outputs. It allows functions to be used as variables for greater flexibility in coding.
    Eg = def apply(func , value):
            return func(value)"""


screen.exitonclick()