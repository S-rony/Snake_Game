from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_squares = []
        self.snake()
        self.head = self.all_squares[0]

    def snake(self):
        x = [0, -20, -40]
        for i in range(3):
            tim = Turtle(shape="square")
            tim.color("blue")
            self.all_squares.append(tim)
            self.all_squares[i].penup()
            self.all_squares[i].goto(x[i], 0)

    def extend(self):
        new_square = Turtle(shape="square")
        new_square.color("blue")
        new_square.penup()
        new_square.goto(self.all_squares[-1].position()) #.position() is another built-in method of the Turtle class — it
        # comes from the same turtle module, just like .goto(), .distance(), .forward(), etc.
        self.all_squares.append(new_square)

    def snake_move(self):
        for square in range(len(self.all_squares) - 1, 0, -1):
            new_x = self.all_squares[square - 1].xcor()
            new_y = self.all_squares[square - 1].ycor()
            self.all_squares[square].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
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
