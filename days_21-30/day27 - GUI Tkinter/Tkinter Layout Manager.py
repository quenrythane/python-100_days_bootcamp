import tkinter as tk

FONT = "Arial", 24, "bold"

window = tk.Tk()
window.title("My first GUI Program")
window.minsize(500, 300)

# Labels
my_label = tk.Label(text="I am a label", font=FONT)
# changing cinfig of object
my_label["text"] = "I am a label with new text"
my_label.config(text="I am a label 2")
# Packer
my_label.pack(side="left")
# my_label.pack(expand=True)

# Button
def button_clicked():
    print("I got clicked")
    text = input.get()
    my_label["text"] = text

button = tk.Button(text="Click Me", command=button_clicked)
button.pack(side="left")

# Entry
input = tk.Entry(width=10)
input.pack()
