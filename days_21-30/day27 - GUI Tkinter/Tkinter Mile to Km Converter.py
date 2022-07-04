from tkinter import *

FONT = "Arial", 20, "bold"
PADX = 20
PADY = 5

window = Tk()
window.title("Mile/Km Converter")
window.minsize(500, 200)
window.maxsize(500, 200)
window.config(padx=PADX, pady=20)


# Miles Section
input = Entry(width=20)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT, padx=PADX)
miles_label.grid(column=2, row=0)


# Km Section
label = Label(text="is equal to", font=FONT, padx=PADX, pady=PADY)
label.grid(column=0, row=1)

number = 0
km_number_label = Label(text=number, font=FONT)
km_number_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


# Button
def button_clicked():
    number = float(input.get())
    km_number_label["text"] = round(number * 1.609, 2)

button = Button(text="Calculate", font=("Arial", 16, "bold"), command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
