import time
from turtle import Turtle


class Score(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(position)
        self.color(color)

    def update_scoreboard(self, score):
        self.clear()
        self.write(score, align="center", font=("Arial", 80, "normal"))
