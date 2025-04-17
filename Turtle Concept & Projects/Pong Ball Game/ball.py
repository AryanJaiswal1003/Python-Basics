#TODO-4: Create the ball & make it move
from turtle import Turtle
import random

colors = ["SteelBlue" , "PaleGreen" , "OliveDrab" , "DarkOrange" , "Gold" , "Maroon" , "DarkMagenta" ,
           "MediumVioletRed" , "Indigo" , "DarkSlateBlue" , "LightCoral" , "OrangeRed" , "Firebrick" ,
          "DarkGoldenrod", "OldLace" , "DarkSlateGray" , "LightSkyBlue" , "MediumSpringGreen" , "SlateGray"]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.shape('circle')
        self.shapesize(stretch_wid=1 , stretch_len=1) #Turtle is 20 * 20 pixels
        self.setposition(x=0 , y=0)
        self.penup()
        self.x_move = 10 #Ball movt across x_axis
        self.y_move = 10 #Ball movt across y_axis
        self.move_speed = 0.1 #Normal speed of the ball

    def right_ball_movt(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x , y=new_y)

    # TODO-5: Detect collision with wall and bounce
    def bounce_y(self):
        self.y_move *= -1

    # TODO-6: Detect ball collision with paddle
    def bounce_x(self):
        self.color(random.choice(colors))
        self.x_move *= -1
        self.move_speed *= 0.9 #Increasing the speed of the ball in the game when each player is playing well

    # TODO-7: Detect when paddle misses the ball
    def reset_position(self):
        self.goto(x=0 , y=0)
        self.move_speed = 0.1 #Resetting the speed if game starts fresh
        self.bounce_x()