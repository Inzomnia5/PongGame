from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(1, 5)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() > 230:  # Cannot move up if paddle is at top
            pass
        else:
            self.forward(20)

    def move_down(self):
        if self.ycor() < -230:  # Cannot move down if paddle is at bottom
            pass
        else:
            self.backward(20)
