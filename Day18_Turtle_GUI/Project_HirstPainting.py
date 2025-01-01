import colorgram

import random
import turtle
from turtle import Turtle, Screen

# Extract 25 colors from an image.
# number_of_colors = 25
# colors = colorgram.extract('img.jpg', number_of_colors)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s


def pick_colors_from_img(number_of_colors, img_name):
    colors = colorgram.extract(img_name, number_of_colors)

    rgb_colors_from_jpg = []

    for n in range(number_of_colors):
        rgb_tuple = (colors[n].rgb[0], colors[n].rgb[1], colors[n].rgb[2])
        rgb_colors_from_jpg.append(rgb_tuple)

    # print(rgb_colors_from_jpg)
    # print(len(rgb_colors_from_jpg))

    return rgb_colors_from_jpg


rgb_list = pick_colors_from_img(27, 'img.jpg')


tim = Turtle()

# tim.shape("turtle")
tim.hideturtle()
tim.penup()
tim_start_position_horizontal = -225
tim_start_position_vertical = -225
tim.goto(tim_start_position_horizontal, tim_start_position_vertical)

turtle.colormode(255)
# tim.pensize(5)
tim.speed("fastest")


def turtle_pick_random_color_for_circle(_rgb_list):
    _rgb = random.choice(_rgb_list)
    return _rgb


def draw_and_fill_circle(rgb_for_circle_filling):
    tim.fillcolor(rgb_for_circle_filling)
    tim.color(rgb_for_circle_filling)
    tim.begin_fill()
    tim.circle(20)
    tim.end_fill()


change_position_up = 0
for move_vertically in range(10):
    for move_horizontally in range(10):
        # tim.pendown()
        tim.dot(20, turtle_pick_random_color_for_circle(rgb_list))
        # draw_and_fill_circle(turtle_pick_random_color_for_circle(rgb_list))
        # tim.penup()
        tim.forward(50)

    change_position_up += 50
    tim.goto(tim_start_position_horizontal, tim_start_position_vertical + change_position_up)


screen = Screen()
screen.screensize(250, 250)
screen.exitonclick()
