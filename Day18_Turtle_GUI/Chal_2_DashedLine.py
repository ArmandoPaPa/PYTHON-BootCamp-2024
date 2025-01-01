from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("green")


def turtle_dashed_line():
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


for number_of_steps in range(14):
    turtle_dashed_line()

screen = Screen()
screen.exitonclick()