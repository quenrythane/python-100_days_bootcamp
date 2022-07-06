import json
import pyperclip as ppc
from random import *
from string import *
from tkinter import *
from tkinter import messagebox as msg  # need to inport "submodule"

base_username = "artur.babinski.g@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)

    password_letters = [choice(ascii_letters) for _ in range(randint(16, 24))]
    password_numbers = [choice(digits) for _ in range(randint(8, 12))]
    password_symbols = [choice(punctuation) for _ in range(randint(8, 12))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    ppc.copy(password)  # automatically copy to generated password to clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website, username, password = website_input.get(), username_input.get(), password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        msg.showinfo(title="Ooops", message="Please, don't leave any fields empty!")
        is_ok = False

    else:
        is_ok = msg.askokcancel(title=website_input.get(),
                                message=f"There are the details entered for page: {website}: \n"
                                        f"Username: {username}, \npassword: {password} \n\nIs it ok to save?")

    if is_ok:
        new_data = {
            website: {
                "username": username,
                "password": password
            }
        }

        try:
            with open("data_password.json", "r") as data_file:
                try:
                    data = json.load(data_file)
                except json.decoder.JSONDecodeError:  # if file is empty
                    data = {}

        except FileNotFoundError:
            with open("data_password.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data_password.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


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

password_input = Entry(text="", width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)


# add section
add_button = Button(text="Add", width=34, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
