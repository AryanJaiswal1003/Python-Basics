from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.go_to_start()
        self.setheading(to_angle=90)

    # TODO-1: Move the turtle with keypress
    def movement(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor() , y=new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)