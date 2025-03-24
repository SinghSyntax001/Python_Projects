import time
from turtle import Screen,Turtle
from Player import Player
from CarManager import CarManager
from ScoreBoard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Welcome Message
welcome = Turtle()
welcome.hideturtle()
welcome.color("black")
welcome.penup()
welcome.goto(0, 0)
welcome.write("Welcome to Turtle Crossing Game!\nPress Enter to play", align="center", font=("Arial", 24, "normal"))

# Variables
is_game_on = False

# Function to Start Game
def start_game():
    global is_game_on
    is_game_on = True
    welcome.clear()

# Listen for Enter Key to Start
screen.listen()
screen.onkey(start_game, "Return")

# Wait for Game Start
while not is_game_on:
    screen.update()


player = Player((0,-280))
cars = CarManager()
score = Scoreboard()

screen.onkey(player.up, "w")



while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.createCar()
    cars.moveCars()

    #detection of finish line
    if player.is_at_finish_line():
        score.increase_score()
        cars.increaseSpeed()
        player.go_to_start()



    #detection of collision with cars
    for car in cars.cars:
        if car.distance(player)<20:
            score.game_over()
            is_game_on = False


screen.exitonclick()
