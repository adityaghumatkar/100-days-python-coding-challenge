from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(3)


def draw_shapes(num_of_sides):
    angel = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angel)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_color = (r, g, b)
    return rgb_color


for shapes_side_n in range(3, 11):
    tim.color(random_color())
    draw_shapes(shapes_side_n)

screen.exitonclick()
