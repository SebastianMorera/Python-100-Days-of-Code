import tkinter
from tkinter import PhotoImage, messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"Website: {website} | Username: {email} | Password: {password}\n")
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Image canvas
canvas = tkinter.Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = tkinter.Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = tkinter.Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = tkinter.Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_entry = tkinter.Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "smorera@gmail.com")
password_entry = tkinter.Entry(width=19)
password_entry.grid(column=1, row=3)

# Buttons
gen_password_button = tkinter.Button(text="Generate Password", width=12, command=generate_password)
gen_password_button.grid(column=2, row=3)
add_button = tkinter.Button(text="Add", width=34, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()