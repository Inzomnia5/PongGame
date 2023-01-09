from turtle import Turtle
GRID_COLOR_LEFT = "purple"
GRID_COLOR_RIGHT = "green"


class GameField:
    def __init__(self):
        grid_pen = Turtle()
        grid_pen.color(GRID_COLOR_LEFT)
        grid_pen.speed(0)
        grid_pen.hideturtle()
        grid_pen.penup()
        grid_pen.goto(-380, -300)
        grid_pen.pendown()

        draw_line = 0
        while grid_pen.xcor() < 600:
            grid_pen.setheading(90)  # up 600
            grid_pen.forward(600)
            draw_line += 1
            grid_pen.setheading(0)  # right 20
            grid_pen.forward(20)
            grid_pen.setheading(270)  # down 600
            grid_pen.forward(600)
            draw_line += 1
            grid_pen.setheading(0)  # right 20
            grid_pen.forward(20)
            if draw_line == 20:
                grid_pen.color(GRID_COLOR_RIGHT)
