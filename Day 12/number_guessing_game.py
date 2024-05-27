import random
from art import logo


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return 10
    else:
        return 5


def check_answer(guess, answer, lives):
    if guess > answer:
        print("Too high.")
        return lives - 1
    elif guess < answer:
        print("Too low..")
        return lives - 1


def number_guessing_game():
    print(logo)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    lives = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == answer:
            print(f"You win 😁! The answer was {answer}.")
            return
        else:
            lives = check_answer(guess, answer, lives)
            if lives == 0:
                print(f"You've run out of guesses, the correct answer was {answer} 😭")
                return
            elif guess != answer:
                print("Guess again.")


if __name__ == '__main__':
    number_guessing_game()
