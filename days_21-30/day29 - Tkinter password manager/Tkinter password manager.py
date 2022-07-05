from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(600, 500)
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# website section
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)

# username section
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2)

# password section
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password = ""
password_input = Entry(text=password, width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15, command=print, padx=0)
generate_button.grid(column=2, row=3)

# add section
add_button = Button(text="Add", width=34)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
