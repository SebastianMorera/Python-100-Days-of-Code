import pandas

def nato_alphabet():
    # TODO 1. Create a dictionary in this format:
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

    # TODO 2. Create a list of the phonetic code words from a word that the user inputs.
    user_word = input("Enter a word: ").upper()
    phonetic_alphabet_code_word = [phonetic_dict[letter] for letter in user_word]

    print(phonetic_alphabet_code_word)

if __name__ == '__main__':
    nato_alphabet()