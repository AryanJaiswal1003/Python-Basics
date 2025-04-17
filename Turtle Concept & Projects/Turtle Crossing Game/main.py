import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('lightblue')
screen.tracer(0)

#TODO-1: Move the turtle with keypress
player= Player()
screen.listen()
screen.onkey(key="Up" , fun=player.movement)

#TODO-2: Create & move the cars
car = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move()

    # TODO-3: Detect collision with cars
    for char in car.all_cars:
        if char.distance(player) < 25:
            game_is_on = False
            score.game_over()

    # TODO-4: Detect when turtle reaches the other side
    if player.ycor() > 280:
        player.go_to_start()
        car.next_level()

        # TODO-5: Create a Scoreboard
        score.updated_score()

















screen.exitonclick()