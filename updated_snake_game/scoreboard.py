with open("data.txt") as file:
    file = int(file.read())
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
        self.high_score = file

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=("Arial", 24, "bold"))
    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as df:
                df.write(str(self.high_score))
        self.score = 0
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=("Consolas", 24, "bold"))