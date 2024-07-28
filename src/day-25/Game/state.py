from turtle import Turtle


class State(Turtle):

    def __init__(self, x_cor, y_cor, state_name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.x = x_cor
        self.y = y_cor
        self.name = state_name
        self.goto(self.x, self.y)
        self.write(self.name)
