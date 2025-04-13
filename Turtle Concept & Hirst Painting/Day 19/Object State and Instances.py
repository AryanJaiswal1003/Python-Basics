"""Object State & Instances --> Turtle Race"""
from turtle import Turtle , Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500 , height=400) #Setting the dimensions for the output display
user_bet = screen.textinput(title="Make Your Bet" , prompt="Which Turtle will win the Race? Enter a Color: ") #screen.textinput
    # works similar to the input function, capturing user response

colors = ["red" , "orange" , "yellow" , "green" , "blue" , "purple"]
y_positions = [-70 , -40 , -10 , 20 , 50 , 80]
all_turtles = []
screen.bgcolor("darkgrey")

for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-240, y=y_positions[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
   for turtle in all_turtles:
       rand_distance = random.randint(0 , 10)
       turtle.forward(rand_distance)
       if turtle.xcor() > 230: #240 - (40 / 2) --> Turtle icon in output is 40 * 40 object
           is_race_on = False
           winning_turtle = turtle.pencolor()
           if winning_turtle == user_bet:
               print(f"You've Won!!! Congratulations. The {winning_turtle} turtle is the Winner.")
           elif winning_turtle != user_bet:
               print(f"You've Lost!!! Try Again. The {winning_turtle} turtle is the Winner.")
           else:
               print(f"It's a Draw!!! The {winning_turtle} turtle is the Winner")

screen.exitonclick()