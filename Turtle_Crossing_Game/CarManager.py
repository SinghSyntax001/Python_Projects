from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class CarManager:
    def __init__(self):
        self.cars = []
        self.createCar()

    def randomColor(self):
        return random.choice(COLORS)  # Use predefined colors

    def randomPosition(self):
        x = 300  # Cars start from the right side
        y = random.randint(-240, 240)  # Random y-position within the screen
        return x, y

    def createCar(self):
        random_chance = random.randint(1, 4)
        if random_chance == 1:

            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Make it look like a car
            new_car.color(self.randomColor())  # Assign random color
            new_car.penup()
            new_car.goto(self.randomPosition())  # Assign random position
            self.cars.append(new_car)  # Add to car list

    def moveCars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)  # Move all cars left

    def increaseSpeed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT  # Increase speed over time
