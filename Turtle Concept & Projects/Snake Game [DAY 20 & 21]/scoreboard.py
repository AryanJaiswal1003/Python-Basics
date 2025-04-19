from turtle import Turtle

#TODO-6: Creating a Scoreboard which returns scores once snake hits food using Turtle.write & Turtle.clear function

ALIGNMENT = "center"
FONT = ("Times New Roman", 15, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x= 0 , y= 270)
        self.color("white")
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score:{self.score}  High Score:{self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self): #Adding High Score function to the program [Day 24]
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(x= 0 , y= 0)
    #     self.write(arg="**** GAME OVER ****", move=False, align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.update_scoreboard()
