import time #Time Module
from turtle import Screen
from snake import Snakes
from food import Food
from scoreboard import ScoreBoard

#Setting up the Screen Configurations.
screen = Screen()
screen.setup(width=600 , height=600)
screen.bgcolor('black')
screen.title(titlestring="My Snake Game")
screen.tracer(n=0)

"""The screen.tracer() --> manages frequency of screen updates for during animations. By default, screen updates after 
    each turtle movt, but with tracer(n) --> you can limit updates to occur every n movt's. 
        Setting tracer(0) --> completely stops automatic updates, & allows manual refresh screen with screen.update()"""

snake = Snakes()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

game_on = True
while game_on:
    screen.update()  ##screen.tracer()
    time.sleep(0.2)  # --> pauses program's execution for a specified number of seconds, allowing delays/timed actions.
    snake.move()

    #TODO-5: Detecting Collision with Food using Turtle.distance function
    #TODO-6: Creating a Scoreboard which returns scores once the snake hits the food using Turtle.write function
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_count()

    #TODO-7: Detecting collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        #scoreboard.game_over()
        scoreboard.reset()
        snake.reset()

    #TODO-9: Detecting Collision with Snake --> if head collides with any segment in tail --> using slicing

    """Slicing = way to extract a subset of elements from sequences like strings, lists, or tuples -- > sequence[start:stop:step]
    --> start: is the index where the slice begins (inclusive).
    --> stop: is the index where the slice ends (exclusive).
    --> step: determines how many elements to skip between indices (optional)."""

    for segment in snake.segments[1:]: #Slicing off the head segment from a collision error
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:  # Check if a segment is too close to any segment
            #game_on = False --> Exit the loop as collision is already detected
            scoreboard.reset()
            snake.reset()

screen.exitonclick()