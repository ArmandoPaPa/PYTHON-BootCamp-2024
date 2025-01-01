import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
turtle.colormode(255)
# tim.color("green")


def turtle_draw_shape(shape_lines: int):
    tim.forward(100)
    tim.left(360 / shape_lines)
 

for num_of_lines_in_shape in range(3, 10):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)
    for _ in range(0, num_of_lines_in_shape):
        turtle_draw_shape(num_of_lines_in_shape)

screen = Screen()
screen.exitonclick()
