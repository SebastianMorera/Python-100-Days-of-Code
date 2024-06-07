from turtle import Turtle, Screen
import random

colors = ["orange red", "lime", "black", "magenta", "yellow", "blue", "medium violet red", "light sea green", "spring"
                                                                                                              "green",
          "indigo"]

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)

    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)


if __name__ == '__main__':
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.speed("fast")
    my_screen = Screen()

    # Challenge 1
    # for _ in range(4):
    #     my_turtle.right(90)
    #     my_turtle.forward(100)

    # Challenge 2
    # for _ in range(8):
    #     my_turtle.pendown()
    #     my_turtle.forward(10)
    #     my_turtle.penup()
    #     my_turtle.forward(10)

    # Challenge 3
    # for i in range(3, 10):
    #     for sides in range(1, i + 1):
    #         my_turtle.color(random.choice(colors))
    #         my_turtle.forward(100)
    #         my_turtle.right(360 / i)

    # Challenge 4
    # my_turtle.pensize(10)
    # my_turtle.speed("fast")
    # for _ in range(200):
    #     my_turtle.color(random.choice(colors))
    #     my_turtle.forward(20)
    #     my_turtle.setheading(random.choice(directions))

    # Challenge 4.5
    # my_screen.colormode(255)
    # my_turtle.pensize(10)
    # my_turtle.speed("fast")
    # for _ in range(200):
    #     my_turtle.color(random_color())
    #     my_turtle.forward(20)
    #     my_turtle.setheading(random.choice(directions))

    # Challenge 5
    my_screen.colormode(255)
    draw_spirograph(5)

    my_screen.exitonclick()
