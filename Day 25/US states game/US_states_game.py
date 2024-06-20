import turtle
import pandas


def us_states_game():
    screen = turtle.Screen()
    screen.title("U.S. States Game")

    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    us_data = pandas.read_csv("50_states.csv")
    all_states = us_data.state.to_list()
    guessed_states = []

    while len(guessed_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                        prompt="What's another state's name?").title()

        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)

            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            break

        if answer_state in all_states:
            guessed_states.append(answer_state)
            turtle_state = turtle.Turtle()
            turtle_state.hideturtle()
            turtle_state.penup()

            state_data = us_data[us_data.state == answer_state]
            turtle_state.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            turtle_state.write(answer_state)


if __name__ == '__main__':
    us_states_game()
