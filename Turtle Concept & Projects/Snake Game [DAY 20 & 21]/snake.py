from turtle import Turtle , Screen

screen = Screen()
STARTING_COORDINATES = [(0, 0), (-20, 0), (-40, 0)] #since turtle dimensions is 20 * 20 pixels
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
"""Constants are fixed values that should not change during a program's execution. Python doesn't enforce constants 
    but uses a convention of writing them in **ALL CAPS** to distinguish from variables written in small caps."""

class Snakes:
    def __init__(self):
        self.snake = None
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # TODO-1: Create a Snake Body --> Square Shaped, 3 in Numbers, Stacked Side by Side, White Color.
    def create_snake(self):
        for coordinate in STARTING_COORDINATES:
            self.add_segment(coordinate)

    #TODO-8: Adding new segment whenever snake hits food
    def add_segment(self , coordinate):
        self.snake = Turtle("square")
        self.snake.color("white")
        self.snake.penup()
        self.snake.goto(coordinate)
        self.segments.append(self.snake)

    def extend(self): #adds a new segment to the snake
        self.add_segment(coordinate=self.segments[-1].position())

    # TODO-2: Moving the snake continuously w/o any input.
    def move(self):
        for snake_num in range(len(self.segments) - 1 , 0 , -1): #this creates a loop that goes through the indices of snake list
            # from last segment (`len(snake) - 1`) to 2nd segment (`1`), moving backwards (`-1` step).
            # Why this? The snake's body need to follow one in front. Starting from tail ensures no segment overwrites another's position until it has "moved up"
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            # new_x & new_y --> get the position of segment just ahead for current one to follow it.
            self.segments[snake_num].goto(x=new_x, y=new_y)

        self.segments[0].forward(MOVE_DISTANCE)

    #TODO-3: Controlling the movt of the snake via input.

    def up(self):
        if self.head.heading() != DOWN: #Written becoz to prevent complete turnover of snake's head in the game --> not allowed
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
