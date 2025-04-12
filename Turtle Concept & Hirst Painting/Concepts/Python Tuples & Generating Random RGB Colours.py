#TODO-Concept = Python Tuples & Generating Random RGB Colours

"""Python Tuples = A tuple is an unchangeable, ordered collection of items. It is defined using parentheses () &
can hold different types of data. Unlike lists, tuples are 'immutable', i.e. can't modify items after creation."""

"""turtle.colormode() = colormode() sets how colors are represented: **1.0** (RGB as floats 0.0-1.0) or 
    **255** (RGB as integers 0-255)."""

import random
import turtle
from turtle import Turtle , Screen
#RGB Calculator = https://www.w3schools.com/colors/colors_rgb.asp

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

def random_color():
    r = random.randint(0 , 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r , g , b)
    return my_tuple


direction = [0 , 90 , 180 , 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(1000):
    tim.forward(20)
    tim.color(random_color())
    tim.setheading(random.choice(direction))


screen = Screen()
screen.exitonclick()