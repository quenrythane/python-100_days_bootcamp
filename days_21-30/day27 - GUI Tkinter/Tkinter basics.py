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


# Text - multiline text
text = tk.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tk.END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", tk.END))
text.pack()

# Spinbox - like input but with arrows - more/less
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale - like slider
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton - like checkbox
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton - like few checkboxes when you could choose only one
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox - list of thinks you could check
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()




window.mainloop()
