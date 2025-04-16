from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#TODO-1: Create the Screen
screen = Screen()
screen.setup(width=800 , height=600)
screen.title(titlestring='Pong Game')
screen.bgcolor('black')
screen.tracer(n=0)

#TODO-2: Create and Move a paddle --> Created a class
r_paddle = Paddle(x_cor=350 , y_cor=0)

#TODO-3: Create another paddle --> added parameters to the __init__ function
l_paddle = Paddle(x_cor=-350 , y_cor=0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up' , fun=r_paddle.up)
screen.onkey(key='Down' , fun=r_paddle.down)
screen.onkey(key='w' , fun=l_paddle.up)
screen.onkey(key='d' , fun=l_paddle.down)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.right_ball_movt()

    # TODO-5: Detect ball collision with wall and bounce
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # TODO-6: Detect ball collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    # TODO-8: Score keeping
    # TODO-7: Detect when r_paddle misses the ball & increasing l_point
    if ball.xcor() > 410:
        ball.reset_position()
        scoreboard.l_point()

    # TODO-7: Detect when l_paddle misses the ball & increasing r_point
    if ball.xcor() < -410:
        ball.reset_position()
        scoreboard.r_point()









screen.exitonclick()