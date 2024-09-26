import pandas

def nato_alphabet():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

    valid_word = False
    phonetic_alphabet_code_word = None

    while not valid_word:
        try:
            user_word = input("Enter a word: ").upper()
            phonetic_alphabet_code_word = [phonetic_dict[letter] for letter in user_word]
            valid_word = True
        except KeyError:
            print("Sorry, only letters in the alphabet please.")

    print(phonetic_alphabet_code_word)

if __name__ == '__main__':
    nato_alphabet()