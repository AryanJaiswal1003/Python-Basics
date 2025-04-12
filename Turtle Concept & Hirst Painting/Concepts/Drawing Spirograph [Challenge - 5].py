"""Challenge-5: Drawing a Spirograph"""

import random
import turtle
from turtle import Turtle , Screen
tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)

def diff_colors():
    r = random.randint(0 , 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r , g , b)
    return my_tuple

tim.speed("fastest")

""" ****** [My Way] ****** """
# for _ in range(100):
#     tim.color(diff_colors())
#     tim.right(5)
#     tim.circle(100)

""" ****** [Teacher's Correct Way] ****** """
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(diff_colors())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)

draw_spirograph(2)


screen = Screen()
screen.exitonclick()