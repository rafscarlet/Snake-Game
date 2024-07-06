# TODO Part 1:
# - Create snake body
# - Move the snake
# - Control the snake
# TODO Part 2:
# - Collision with food
# - Create scoreboard
# - Collision with wall / tail (game over)

from turtle import Screen
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control the snake
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    head = snake.snake_pieces[0]
    
    # Detect collision with food
    if head.distance(food) < 15:
        food.relocate()
        scoreboard.increase()
        snake.extend()

    # Detect collision with wall
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        snake.reset()
        scoreboard.reset_score()
        # game_on = False
        # scoreboard.game_over()

    # Detect collision with tail
    for i in snake.snake_pieces[1:]:
        if head.distance(i.pos()) < 10:
            snake.reset()
            scoreboard.reset_score()
            # game_on = False
            # scoreboard.game_over()

screen.exitonclick()
