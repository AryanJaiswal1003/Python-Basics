""" ********* Hirst Painting Project [Part-2] ********* """
import turtle

#TODO-4: Using turtle & extracted color list --> create a spot painting
"""Requirements => 1. 10 * 10 rows of spot
                   2. Dot size 20.
                   3. Space b/w 2 spot is 50 paces"""

from color import color_output_list
from turtle import Turtle , Screen
import random

tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.speed("fastest")
turtle.colormode(255) #Imp to include this

#Sets the Turtle to start from bottom screen
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

""" ****** [Method-1] ****** """
for _ in range(109):
    if tim.xcor() == 287.86796564403573:
        tim.backward(500)
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(0)
    else:
        tim.dot(20, random.choice(color_output_list))
        tim.fd(50)

    #Written to know the Coordinates of the Turtle
        x = tim.xcor()
        y = tim.ycor()
        ab = (x, y)
        print(ab)


""" ****** [Method-2] ****** """
def hirst_painting(space):
    for _ in range(space):
        for _ in range(space):
            tim.fd(50)
            tim.dot(20 , random.choice(color_output_list))
        tim.backward(space * 50)
        tim.left(90)
        tim.fd(50)
        tim.right(90)

hirst_painting(10)


""" ****** [Method-3] ****** """
number_of_dots = 100

for dot_count in range(1 , number_of_dots + 1):
    tim.dot(20 , random.choice(color_output_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90) #or --> tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

tim.hideturtle()

screen.exitonclick()