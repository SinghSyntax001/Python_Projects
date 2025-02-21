from turtle import Turtle 
import random as rn


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x = rn.randint(-275,275)
        random_y = rn.randint(-275,250)
        self.goto(random_x, random_y)

    
        