from turtle import Turtle

STARTING_POINT = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.go_to_start()
        self.setheading(UP)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POINT)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False




    

    

        