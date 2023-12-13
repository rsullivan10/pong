from turtle import Turtle


class Ball(Turtle):

    def __init__(self,position):
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
