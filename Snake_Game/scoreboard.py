from turtle import Turtle 
ALIGNMENT = "Center"
FONT = ('Arial', 25, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,260)
        
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
                self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score +=1
        self.clear()
        self.updateScore()
    
    def gameOver(self):
          self.goto(0,0)
          self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    
    