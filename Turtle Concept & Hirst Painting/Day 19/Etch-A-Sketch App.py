#TODO = Etch-A-Sketch App Project

"""Requirements --> 'W' = Forwards , 'S' = Backwards , 'A' = Counter-clockwise , 'D' = Clockwise , 'C' = Clear Drawing"""

from turtle import Turtle , Screen

tim = Turtle()
tim.shape("turtle")
tim.speed("fast")

screen = Screen()
tim.pensize(3)

def forward_movt():
    tim.forward(20)

def backward_movt():
    tim.backward(20)

def counter_clockwise_movt():
    tim.left(20)
    #Also --> new_heading = tim.heading() + 20
    #         tim.setheading(new_heading)

def clockwise_movt():
    tim.right(20)
    # Also --> new_heading = tim.heading() - 20
    #         tim.setheading(new_heading)

def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w" , fun=forward_movt)
screen.onkey(key="s" , fun=backward_movt)
screen.onkey(key="a" , fun=counter_clockwise_movt)
screen.onkey(key="d" , fun=clockwise_movt)
screen.onkey(key="c" , fun=clear_drawing)

screen.exitonclick()