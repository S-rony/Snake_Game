from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 20, "normal"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=("Arial", 24, "bold"))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Consolas", 24, "bold"))