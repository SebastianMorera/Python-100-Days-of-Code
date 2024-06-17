from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = False

if __name__ == '__main__':
    my_screen = Screen()
    my_screen.setup(width=500, height=400)
    user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

    all_turtles = []
    y = -70
    for i in range(len(colors)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto((-230, y))
        all_turtles.append(new_turtle)
        y += 30

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")

            rand_dist = random.randint(0, 10)
            turtle.forward(rand_dist)

    my_screen.exitonclick()