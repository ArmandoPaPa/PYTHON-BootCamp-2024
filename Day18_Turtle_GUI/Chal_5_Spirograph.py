import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
turtle.colormode(255)
tim.pensize(5)
tim.speed(5)


def draw_circle():
    turtle.circle(100)


def turtle_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


number_of_circles = 23

for n in range(0, number_of_circles):
    angle = 360 / number_of_circles
    turtle.left(angle)
    turtle.color(turtle_random_color())
    draw_circle()


screen = Screen()
screen.exitonclick()
