import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
turtle.colormode(255)
tim.pensize(8)
tim.speed(5)


def turtle_random_walk():
    walk_direction = random.choice(['f', 'b', 'l', 'r'])
    if walk_direction == 'f':
        tim.forward(23)
    elif walk_direction == 'b':
        tim.backward(23)
    elif walk_direction == 'l':
        tim.left(90)
        tim.forward(23)
    elif walk_direction == 'r':
        tim.right(90)
        tim.forward(23)
    else:
        print("Something unexpected happened. Sorry.")


def turtle_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r, g, b)


for step in range(100):
    turtle_random_color()
    turtle_random_walk()


screen = Screen()
screen.exitonclick()
