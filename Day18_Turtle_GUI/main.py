from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("green")


def turtle_turn_and_move():
    tim.forward(100)
    tim.left(90)


for number_of_turns in range(0, 4):
    turtle_turn_and_move()

screen = Screen()
screen.exitonclick()
