from turtle import Turtle

#TODO-8: Score keeping
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(arg=self.l_score, align="center", font=("Times New Roman", 70, "normal"))
        self.goto(x=100, y=200)
        self.write(arg=self.r_score, align="center", font=("Times New Roman", 70, "normal"))

    # TODO-7: Detect when r_paddle misses the ball & increasing l_point
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    # TODO-7: Detect when l_paddle misses the ball & increasing r_point
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
