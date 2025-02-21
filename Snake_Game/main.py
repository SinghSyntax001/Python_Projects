
from turtle import Turtle, Screen
from snake import Snake
from food import Food
import time
from scoreboard import ScoreBoard

welcome = Turtle()
welcome.hideturtle()
welcome.color("white")
welcome.penup()
welcome.goto(0, 0)
welcome.write("Welcome to Snake Game!\nPress Enter to play", align="center", font=("Arial", 24, "normal"))

screen = Screen()
screen.title("The Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

is_game_on = False
def start_game():
    global is_game_on
    is_game_on = True
    welcome.clear()  

screen.listen()
screen.onkey(start_game, "Return")

while not is_game_on:
    screen.update()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

delay=0.1
while is_game_on:
    screen.update()
    time.sleep(delay)
    snake.move()

    #detect collision with food
    if(snake.head.distance(food)<15):
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()
        delay *=1
        
    
    #detect collision with wall
    if(snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280):
        is_game_on=False
        scoreboard.gameOver()

    #detect collision with tail
    for tail in snake.snake[1:]:
        if snake.head.distance(tail)<10:
            is_game_on = False
            scoreboard.gameOver()

screen.exitonclick()