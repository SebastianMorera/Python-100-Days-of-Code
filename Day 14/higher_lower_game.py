from art import logo, vs
from game_data import data
from replit import clear
import random


def format_data(values):
    name = values["name"]
    follower_count = values["follower_count"]
    description = values["description"]
    country = values["country"]

    return name, follower_count, description, country


def check_answer(guess, follower_count1, follower_count2, score, correct_answer):
    if guess == "a" and follower_count1 > follower_count2:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
    elif guess == "b" and follower_count2 > follower_count1:
        score += 1
        clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        correct_answer = False
    return score, correct_answer


def higher_lower_game():
    print(logo)
    score = 0
    correct_answer = True

    while correct_answer:
        name1, follower_count1, description1, country1 = format_data(random.choice(data))
        print(f"Compare A: {name1}, a {description1}, from {country1}.")
        print(vs)
        name2, follower_count2, description2, country2 = format_data(random.choice(data))
        print(f"Compare B: {name2}, a {description2}, from {country2}.")

        print(f"Solution is: Follower count 1 = {follower_count1} and Follower count 2 = {follower_count2}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        score, correct_answer = check_answer(guess, follower_count1, follower_count2, score, correct_answer)


if __name__ == '__main__':
    higher_lower_game()
