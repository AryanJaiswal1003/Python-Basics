from turtle import Turtle
FONT = ("Times New Roman", 20, "normal")

#TODO-5: Create a Scoreboard
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 1
        self.initial_score()

    def initial_score(self):
        self.clear()
        self.goto(x=-290, y=260)
        self.write(arg=f"Level: {self.score}", align="Left", font=FONT)

    def updated_score(self):
        self.score += 1
        self.initial_score()

    def game_over(self):
        self.goto(x=0 , y=0)
        self.color('black')
        self.write(arg="***** GAME OVER !!! *****", move=False, align="Center", font=("Times New Roman", 15, "normal"))