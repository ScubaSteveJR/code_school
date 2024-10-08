from turtle import Turtle, Screen
from snake2 import Snake
from food2 import Food
import time
t = Turtle()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

# Snake food

screen.exitonclick()
