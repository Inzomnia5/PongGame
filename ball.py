from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10  # Initial ballSpeed
        self.y_move = 10  # Initial ballSpeed

    def move_ball(self):
        ball_xcor = self.xcor() + self.x_move
        ball_ycor = self.ycor() + self.y_move
        self.setposition(ball_xcor, ball_ycor)

        if 0 < self.xcor() < 350:  # if ball is on RIGHT screen
            self.color("purple")

        if self.xcor() > 0 and self.xcor() == 350:  # if right player missed
            self.color("green")

        if 0 > self.xcor() > -350:  # if ball is on LEFT screen
            self.color("green")

        if self.xcor() < 0 and self.xcor() == -350:  # if right player missed
            self.color("purple")

    def ball_bounce_top_bottom(self):
        self.y_move *= -1

    def ball_bounce_paddle(self):
        self.x_move *= -1

    def ball_reset(self):
        self.setposition(0, 0)
        self.x_move *= -1
        self.color("white")
