def mail_merge():
    with (open("./Input/Names/invited_names.txt", mode="r") as names_file):
        names = names_file.readlines()

    with (open("./Input/Letters/starting_letter.txt", mode="r") as letter_file):
        letter_content = letter_file.read()

    for name in names:
        final_content = letter_content.replace("[name]", name.strip())
        with (open(f"./Output/Ready to send/letter_for_{name.strip()}.txt", mode="w") as completed_letter):
            completed_letter.write(final_content)


if __name__ == '__main__':
    mail_merge()
