from turtle import  Screen

from dask.array import square

from food import Food
from scoreboard import Score
import time
from snake import Snake
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("red")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
# screen.onkey(key="c", fun=clear_screen)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with the Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()



    #Detect collision with the Tail
    # for square in snake.all_squares: ## this will also work
    #     if square == snake.head:
    #         pass
    for square in snake.all_squares[1:]:
        if snake.head.distance(square) < 10:
            score.reset()
            snake.reset()

    # all_squares[0].right(90)

    # for square in all_squares:
    #     square.forward(20)

screen.exitonclick()

