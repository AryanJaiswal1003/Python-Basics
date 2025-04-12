"""Challenge - 4: Random Walk with Random Colour"""
import random
from turtle import Turtle , Screen

t = Turtle()
t.shape("turtle")

angle = [0 , 90 , 180 , 270]
colors = ["SteelBlue" , "PaleGreen" , "OliveDrab" , "DarkOrange" , "Gold" , "Maroon" , "DarkMagenta" ,
           "MediumVioletRed" , "Indigo" , "DarkSlateBlue" , "LightCoral" , "OrangeRed" , "Firebrick" ,
          "DarkGoldenrod", "OldLace" , "DarkSlateGray" , "LightSkyBlue" , "MediumSpringGreen" , "Black" , "SlateGray"]

t.pensize(15)
t.speed("fastest")

for char in range(2000):
    t.forward(20)
    t.color(random.choice(colors))
    t.setheading(random.choice(angle))

screen = Screen()
screen.exitonclick()