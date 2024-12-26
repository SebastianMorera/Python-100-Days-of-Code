import tkinter

def mile_to_kilometers_converter() -> None:
    def calculate_button_clicked():
        print("Calculate clicked")
        miles = float(mile_entry.get())
        km = miles * 1.60934
        result_label.config(text=f"{km}")

    window = tkinter.Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=300, height=100)
    window.config(padx=20, pady=20)

    # Miles entry
    mile_entry = tkinter.Entry(width=8)
    mile_entry.grid(column=2, row=1)

    # Mile Label
    mile_label = tkinter.Label(text="Miles", font=("Arial", 24))
    mile_label.grid(column=3, row=1)

    # is equal to  Label
    equal_to_label = tkinter.Label(text="is equal to", font=("Arial", 24))
    equal_to_label.grid(column=1, row=2)

    # Result label
    result_label = tkinter.Label(text="0", font=("Arial", 24))
    result_label.grid(column=2, row=2)

    # Km label
    km_label = tkinter.Label(text="Km", font=("Arial", 24))
    km_label.grid(column=3, row=2)

    # Calculate button
    calculate_button = tkinter.Button(text="Calculate", command=calculate_button_clicked)
    calculate_button.grid(column=2, row=3)

    window.mainloop()

if __name__ == '__main__':
    mile_to_kilometers_converter()