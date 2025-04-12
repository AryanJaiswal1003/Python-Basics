"""Challenge-3: Drawing Triangle,Square,Pentagon,Hexagon,Heptagon,Octagon,Nonagon & Decagon"""
from turtle import Turtle , Screen
tim = Turtle()
tim.shape("turtle")

"""****** [My Way] ******"""
def shape_triangle(length):
    angle = 360/3
    tim.color("DarkRed")
    for _ in range(3):
        tim.right(angle)
        tim.forward(length)

def shape_square(length):
    angle = 360/4
    tim.color("orange")
    for _ in range(4):
        tim.right(angle)
        tim.forward(length)

def shape_pentagon(length):
    angle = 360/5
    tim.color("yellow3")
    for _ in range(5):
        tim.right(angle)
        tim.forward(length)

def shape_hexagon(length):
    angle = 360/6
    tim.color("DeepSkyBlue4")
    for _ in range(6):
        tim.right(angle)
        tim.forward(length)

def shape_heptagon(length):
    angle = 360/7
    tim.color("HotPink3")
    for _ in range(7):
        tim.right(angle)
        tim.forward(length)

def shape_octagon(length):
    angle = 360/8
    tim.color("LimeGreen")
    for _ in range(8):
        tim.right(angle)
        tim.forward(length)

def shape_nonagon(length):
    angle = 360/9
    tim.color("purple")
    for _ in range(9):
        tim.right(angle)
        tim.forward(length)

def shape_decagon(length):
    angle = 360/10
    tim.color("YellowGreen")
    for _ in range(10):
        tim.right(angle)
        tim.forward(length)

shape_triangle(100)
shape_square(100)
shape_pentagon(100)
shape_hexagon(100)
shape_heptagon(100)
shape_octagon(100)
shape_nonagon(100)
shape_decagon(100)

"""****** [Teacher's Way] ******"""
import random

colours = ["SteelBlue" , "PaleGreen" , "OliveDrab" , "DarkOrange" , "Gold" , "Maroon" , "DarkMagenta" ,
           "MediumVioletRed" , "Indigo" , "DarkSlateBlue"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for sides in range(3 , 11):
    tim.color(random.choice(colours))
    draw_shape(sides)


screen = Screen()
screen.exitonclick()