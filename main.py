#D20 Build the Snake Game!
from turtle import Screen, Turtle
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard
import time

#setup screen, widths, and heights)
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Armand's Snake game!")
#tracer function to turn animation on/off)
screen.tracer(0)

#implement all the objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
  
    screen.update()
    time.sleep(0.05)

    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    
    #detect collision with wall
    #if snake head hits the edge/limit of the wall of the screen, then game over
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.reset()
        snake.reset()
    #detect collision with tail
    for segment in snake.segments:
        if segment ==  snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
        
#exit the turtle screen
screen.exitonclick()