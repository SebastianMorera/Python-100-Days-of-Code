import os.path
import tkinter
from tkinter import PhotoImage, Button
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None

def flash_card_app():
    def next_card():
        global current_card, flip_timer
        if flip_timer is not None:
            window.after_cancel(flip_timer)
        current_card = random.choice(data)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        flip_timer = window.after(3000, func=flip_card)

    def flip_card():
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
        canvas.itemconfig(card_background, image=card_back_img)

    def is_known():
        data.remove(current_card)
        new_data = pandas.DataFrame(data)
        new_data.to_csv("data/words_to_learn.csv", index=False)
        next_card()

    # Dataframe data
    if os.path.exists("data/words_to_learn.csv"):
        data_frame = pandas.read_csv("data/words_to_learn.csv")
    else:
        data_frame = pandas.read_csv("data/french_words.csv")
    data = data_frame.to_dict(orient="records")

    window = tkinter.Tk()
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    flip_timer = window.after(3000, func=flip_card)

    # Card canvas
    canvas = tkinter.Canvas(width=800, height=526)
    card_front_img = PhotoImage(file="images/card_front.png")
    card_back_img = PhotoImage(file="images/card_back.png")
    card_background = canvas.create_image(400, 263, image=card_front_img)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    # Wrong button
    wrong_img = PhotoImage(file="images/wrong.png")
    unknown_button = Button(image=wrong_img, highlightthickness=0,command=next_card)
    unknown_button.grid(column=0, row=1)

    # Right button
    right_img = PhotoImage(file="images/right.png")
    known_button = Button(image=right_img, highlightthickness=0, command=is_known)
    known_button.grid(column=1, row=1)

    next_card()
    window.mainloop()

if __name__ == '__main__':
    flash_card_app()
