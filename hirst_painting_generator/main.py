# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract("img.jpg", 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(252, 244, 248), (219, 153, 107), (133, 171, 195), (222, 72, 88), (215, 131, 149), (24, 119, 152), (241, 208, 98), (121, 177, 149), (38, 119, 84), (20, 165, 204), (219, 83, 76), (140, 86, 62), (131, 83, 102), (175, 185, 215), (21, 168, 123), (161, 209, 166), (174, 154, 74), (3, 96, 115), (237, 161, 174), (238, 166, 152), (54, 59, 93), (152, 207, 220), (102, 126, 174), (40, 56, 76), (34, 87, 53), (232, 209, 16), (74, 79, 40)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()


