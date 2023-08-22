from turtle import Turtle


class Block(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.color("white")
        self.penup()
