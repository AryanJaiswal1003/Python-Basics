"""Challenge - 4: Random Walk with Random Color"""
import random
from turtle import Turtle , Screen

t = Turtle()
t.shape("turtle")
screen = Screen()
screen.bgcolor('black')

angle = [0 , 90 , 180 , 270]
colors = ["SteelBlue" , "PaleGreen" , "OliveDrab" , "DarkOrange" , "Gold" , "Maroon" , "DarkMagenta" ,
           "MediumVioletRed" , "Indigo" , "DarkSlateBlue" , "LightCoral" , "OrangeRed" , "Firebrick" ,
          "DarkGoldenrod", "OldLace" , "DarkSlateGray" , "LightSkyBlue" , "MediumSpringGreen", "SlateGray"]

t.pensize(15)
t.speed("fastest")

for char in range(500):
    t.forward(20)
    t.color(random.choice(colors))
    t.setheading(random.choice(angle))


screen.exitonclick()