from replit import clear
from art import logo


def secret_auction():
    print(logo)
    continue_auction = True
    auction_dict = {}

    while continue_auction:
        name = input("What is your name?\n")
        bid = int(input("What is your bid?\n$"))
        auction_dict[name] = bid
        if input("Are there any other bidders? Type 'yes or 'no'.\n") == "no":
            continue_auction = False
        else:
            clear()
    winner = max(auction_dict, key=auction_dict.get)
    print(f"The winner is {winner} with a bid of ${auction_dict[winner]}")


if __name__ == '__main__':
    secret_auction()
