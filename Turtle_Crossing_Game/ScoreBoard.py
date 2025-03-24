from turtle import Turtle

ALIGNMENT = "left"  # Changed to properly align text
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):  #
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        """Displays the current score on the screen."""
        self.clear()
        self.goto(-260, 260)  # Adjusted Y-position to be visible
        self.write(f"LEVEL: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score and updates the display."""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Displays 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
