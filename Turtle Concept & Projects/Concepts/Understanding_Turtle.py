"""Understanding Turtle Graphics & how to use Documentation"""

from turtle import Turtle , Screen # "*" imports everything

tim = Turtle()
tim.shape("turtle")
# tim.color("black")

"""Challenge-1: Draws a Square"""
# for turtle in range(4):
#     tim.forward(100)
#     tim.right(90)

"""
********** [Aliasing Modules] ************
import turtle as t #here "t" is the alias name
tim = t.Turtle()

*********** [Installing Modules] **************
import heroes #Module saved in "venv or Local Virtual Environment"
# we can install Modules via Terminal Code --> pip install ##Module_Name
print(heroes.gen())"""

"""Challenge-2: Drawing a Dashed Line"""

#TODO - Method 1: Using 'pencolor()' method
# for _ in range(10):
#     tim.forward(10)
#     tim.pencolor("black")
#     tim.forward(10)
#     tim.pencolor("white")

#TODO - Method 2: Using 'penup() --> pu() & pendown() --> pd()' method
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


screen = Screen()
screen.exitonclick()