from turtle import Turtle
import random

"""Class Inheritance in OOP --> feature where a child/sub class derives methods & attributes from parent/base class.
    --> It allows to reuse, extend, or modify func defined in parent class, promoting code reusability & hierarchy.
    --> Using super() func, one can call methods of parent class inside child class."""

colors = ["SteelBlue" , "PaleGreen" , "OliveDrab" , "DarkOrange" , "Gold" , "Maroon" , "DarkMagenta" ,
           "MediumVioletRed" , "Indigo" , "DarkSlateBlue" , "LightCoral" , "OrangeRed" , "Firebrick" ,
          "DarkGoldenrod", "OldLace" , "DarkSlateGray" , "LightSkyBlue" , "MediumSpringGreen" , "SlateGray"]

#TODO-4: Creating Food class with its inheritance from Turtle superclass
class Food(Turtle): #here Turtle is the superclass

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.8 , stretch_wid=0.8) #--> food's dimensions is 10 * 10 pixels
        rand_color = random.choice(colors)
        self.color(rand_color)
        self.speed("fastest")
        random_x = random.randint(-280 , 280) #the size of the screen is 600 * 600 i.e., x & y-axis extends from -300 to 300 coordinates
        random_y = random.randint(-280 , 280) #since food if generated at coordinates 300 will result to collision with wall.
        self.goto(x=random_x , y=random_y)
        self.refresh()

    # TODO-5: Detecting Collision with Food using Turtle.distance function & shifting food to next random location
    def refresh(self):
        random_x = random.randint(-280, 280)  # the size of the screen is 600 * 600 i.e., x & y-axis extends from -300 to 300 coordinates
        random_y = random.randint(-280, 260)
        rand_color = random.choice(colors)
        self.color(rand_color)
        self.goto(x=random_x, y=random_y)