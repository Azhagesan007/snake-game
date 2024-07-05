from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

start = True
s.listen()
s.onkey(key="Up", fun=snake.up)
s.onkey(key="Down", fun=snake.down)
s.onkey(key="Left", fun=snake.left)
s.onkey(key="Right", fun=snake.right)
while start:
    s.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_increases()
        if score.score >= score.high_score:
            score.high_score = score.score
            score.update_scoreboard()
        snake.extend()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score.game_over()
        start = False
    segment = snake.segments[1:]
    for tail in segment:
        if snake.head.distance(tail) < 10:
            score.game_over()
            start = False

s.exitonclick()
