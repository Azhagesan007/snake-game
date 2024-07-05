from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    """It handles the snake part of the game"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for cube_position in POSITION:
            self.add_segment(cube_position)

    def add_segment(self, cube_position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(cube_position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake"""
        for seg_number in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg_number - 1].xcor()
            y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """change the direction of snack upside"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """change the direction of snack downside"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """change the direction of snack left side"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """change the direction of snack right side"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
