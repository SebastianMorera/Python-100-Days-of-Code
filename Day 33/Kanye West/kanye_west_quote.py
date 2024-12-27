import requests
from tkinter import *

KANYE_QUOTES_URL = "https://api.kanye.rest/"


def kanye_quote() -> None:
    def get_quote() -> None:
        response = requests.get(url=KANYE_QUOTES_URL)
        response.raise_for_status()
        data = response.json()
        quote = data["quote"]

        canvas.itemconfig(quote_text, text=quote)

    window = Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=300, height=414)
    background_img = PhotoImage(file="background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="", width=250, font=("Arial", 24, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    kanye_img = PhotoImage(file="kanye.png")
    kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()

if __name__ == '__main__':
    kanye_quote()
