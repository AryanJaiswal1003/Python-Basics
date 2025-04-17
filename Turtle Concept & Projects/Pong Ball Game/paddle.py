from turtle import Turtle

#TODO-2: Create and Move a paddle
#TODO-3: Create another paddle --> added parameters to the __init__ function

class Paddle(Turtle): #Created a Turtle Superclass

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5 , stretch_len=1) #since turtle has a dimension of 20 * 20 pixels --> Requirement of Paddle width = 100 & height = 20
        self.penup()
        self.goto(x=x_cor , y=y_cor)

    def up(self):
        new_y = self.ycor() + 50
        self.goto(self.xcor() , new_y)

    def down(self):
        new_y = self.ycor() - 50
        self.goto(self.xcor(), new_y)
