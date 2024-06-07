import turtle

import colorgram
from turtle import Turtle, Screen
import random

color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152), (16, 22, 55), (66, 9, 49), (240, 245, 251), (244, 39, 149), (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111), (229, 165, 8), (15, 154, 22), (245, 58, 16), (98, 75, 9), (248, 11, 9), (222, 140, 203), (68, 240, 161), (10, 97, 62), (5, 38, 33), (68, 219, 155)]

if __name__ == '__main__':
    # Extract some colors from an Image and remove the white colors
    # colors = colorgram.extract('image.jpg', 30)
    # color_list = []
    # for color in colors:
    #     current_rgb = (color.rgb.r, color.rgb.g, color.rgb.b,)
    #     color_list.append(current_rgb)
    # print(color_list)

    art = Turtle()
    art.hideturtle()
    art.speed('fastest')
    art.penup()
    art.setpos(-200, -200)

    my_screen = Screen()
    my_screen.colormode(255)

    number_of_dots = 100
    for dot_count in range(1, number_of_dots + 1):
        art.dot(20, random.choice(color_list))
        art.forward(50)

        if dot_count % 10 == 0:
            art.setheading(90)
            art.forward(50)
            art.setheading(180)
            art.forward(500)
            art.setheading(0)

    my_screen.exitonclick()
