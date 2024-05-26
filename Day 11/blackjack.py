import random
from replit import clear
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def sum_up_score(player_cards):
    player_score = 0
    for value in player_cards:
        player_score += value
    return player_score


def blackjack():
    continue_playing = True

    while continue_playing:
        game_over = False
        if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "n":
            continue_playing = False
        else:
            clear()
            print(logo)
            user_cards = []
            computer_cards = []
            user_score = 0
            computer_score = 0

            for _ in range(0, 2):
                user_cards.append(deal_card())
                computer_cards.append(deal_card())

            draw_again = True
            while draw_again:
                user_score = sum_up_score(user_cards)
                computer_score = sum_up_score(computer_cards)
                print(f"\tYour cards: {user_cards}, current score: {user_score}")
                print(f"\tComputer's cards: {computer_cards}, current score: {computer_score}")

                if user_score == 21:
                    print("You win with a Blackjack 😎")
                    draw_again = False
                    game_over = True
                elif computer_score == 21:
                    print("You lose 😭 opponent has Blackjack 😱")
                    draw_again = False
                    game_over = True
                elif user_score > 21:
                    if 11 in user_score:
                        if user_score - 11 + 1 > 21:
                            print("You went over. You lose 😭")
                            draw_again = False
                            game_over = True
                    else:
                        print("You went over. You lose 😭")
                        draw_again = False
                        game_over = True
                else:
                    if input("Type 'y' to get another card, type 'n' to pass: ") == "n":
                        draw_again = False
                    else:
                        user_cards.append(deal_card())

            if game_over:
                continue

            print(f"\tYour final hand: {user_cards}, final score: {user_score}")
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score = sum_up_score(computer_cards)

            print(f"\tComputer's final hand: {computer_cards}, final score: {computer_score}")
            if computer_score > 21:
                print("Opponent went over. You win 😁")
            else:
                if user_score == computer_score:
                    print("It's a draw 🤯")
                elif user_score > computer_score:
                    print("You win 😁")
                elif computer_score > user_score:
                    print("You lose 😭")
                elif computer_score == 21:
                    print("You lose 😭 opponent has Blackjack 😱")


if __name__ == '__main__':
    blackjack()
