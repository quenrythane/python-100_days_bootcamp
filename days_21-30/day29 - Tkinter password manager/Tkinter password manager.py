from tkinter import *

base_username = "artur.babinski.g@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open("data_password.csv", "a") as data:
        log = f"{website_input.get()},{username_input.get()},{password_input.get()}\n"
        data.write(log)
        website_input.delete(0, END), password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
# window.minsize(600, 500)
window.config(padx=50, pady=20)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0, columnspan=3, ipadx=0)

# website section
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=40)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()


# username section
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

username_input = Entry(width=40)
username_input.insert(0, base_username)
username_input.grid(column=1, row=2, columnspan=2)


# password section
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password = ""
password_input = Entry(text=password, width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15)
generate_button.grid(column=2, row=3)


# add section
add_button = Button(text="Add", width=34, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
