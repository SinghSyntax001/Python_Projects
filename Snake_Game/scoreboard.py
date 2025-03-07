from turtle import Turtle 
ALIGNMENT = "Center"
FONT = ('Arial', 25, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highScore = 0
        self.color("White")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highScore}", move=False, align=ALIGNMENT, font=FONT)
                
    def reset(self):
        if self.score>self.highScore:
            self.highScore=self.score
        self.score = 0
        self.updateScore()

    def increaseScore(self):
        self.score +=1
        self.clear()
        self.updateScore()
    

    

        

    

    
    
