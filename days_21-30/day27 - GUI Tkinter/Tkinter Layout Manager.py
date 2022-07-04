import tkinter as tk

FONT = "Arial", 24, "bold"

window = tk.Tk()
window.title("My first GUI Program")
window.minsize(600, 300)
window.config(padx=100, pady=200)

"""Layout Manager"""
# Pack
# Place
# Grid - relative to others. When we use grid we could not use place

# Labels
my_label = tk.Label(text="I am a label", font=FONT)
# changing config of object
my_label["text"] = "I am a label with new text"
my_label.config(text="I am a label 2")
my_label.config(padx=50, pady=50)
# Packer
my_label.grid(column=1, row=2)
# my_label.pack(side="left")
# my_label.pack(expand=True)

# Button
def button_clicked():
    print("I got clicked")
    text = input.get()
    my_label["text"] = text

button = tk.Button(text="Click Me", command=button_clicked)
button.place(x=400, y=0)

# Entry
input = tk.Entry(width=10)
input.grid(column=0, row=0)


window.mainloop()

