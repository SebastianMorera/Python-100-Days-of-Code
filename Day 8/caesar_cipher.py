from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar_cipher():
    print(logo)
    stop_game = False

    while not stop_game:
        cipher_text = ""
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        if direction == "decode":
            shift *= -1

        for char in text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position + shift) % len(alphabet)
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        print(f"The {direction} text is {''.join(cipher_text)}")

        play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if play_again == "no":
            stop_game = True
            print("Goodbye!")


if __name__ == '__main__':
    caesar_cipher()
