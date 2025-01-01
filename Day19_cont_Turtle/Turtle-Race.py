import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="MAKE YOUR BET in Turtle Race",
                            prompt="Which turtle will win the race? "
                                   "The following colore are available: "
                                   "'red', 'green', 'blue', 'yellow', 'black'. "
                                   ">>>>> ENTER A COLOR:   ")
print(user_bet)

# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(-250, 150)
#
# tom = Turtle(shape="turtle")
# tom.penup()
# tom.goto(-250, 75)
#
# jane = Turtle(shape="turtle")
# jane.penup()
# jane.goto(-250, 0)
#
# jake = Turtle(shape="turtle")
# jake.penup()
# jake.goto(-250, -75)
#
# jack = Turtle(shape="turtle")
# jack.penup()
# jack.goto(-250, -150)


# turtle.colormode(255)

# def turtle_random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b


y_positions = [150, 75, 0, -75, -150]
colors = ["red", "green", "blue", "yellow", "black"]
all_turtles = []

for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-280, y_positions[turtle_index])
    all_turtles.append(new_turtle)


# tim.color(user_bet)
# tom.color(turtle_random_color())
# jane.color(turtle_random_color())
# jake.color(turtle_random_color())
# jack.color(turtle_random_color())


# def turtle_walk():
#     tim.forward(random.randint(5, 50))
    # tom.forward(random.randint(5, 50))
    # jane.forward(random.randint(5, 50))
    # jake.forward(random.randint(5, 50))
    # jack.forward(random.randint(5, 50))

# turtle_walk()


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 260:
            is_race_on = False
            print(turtle.pencolor())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(1, 20)
        turtle.forward(rand_distance)


screen.exitonclick()
