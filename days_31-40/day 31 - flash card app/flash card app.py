from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Arial", 48, "italic")
FONT_2 = ("Arial", 60, "bold")
curren_word = ""

# read csv
try:
    data_dict = pd.read_csv("data/french_words_to_learn.csv").to_dict()
except FileNotFoundError:
    data_dict = pd.read_csv("data/french_words.csv").to_dict()  # French: {int: "word"}

# french_word: english_word
data_dict = {data_dict["French"][index]: data_dict["English"][index] for index in range(len(data_dict["French"]))}


def flip_card(random_french_word):
    flashcard.itemconfig(card_language, text="English", fill="white")
    flashcard.itemconfig(card_word, text=data_dict[random_french_word], fill="white")
    flashcard.itemconfig(card_image, image=image_back)


def next_card():
    global flip_timer, curren_word
    window.after_cancel(flip_timer)
    curren_word = random.choice(list(data_dict.keys()))
    flashcard.itemconfig(card_image, image=image_front)
    flashcard.itemconfig(card_language, text="French", fill="black")
    flashcard.itemconfig(card_word, text=curren_word, fill="black")
    flip_timer = window.after(3000, flip_card, curren_word)


def is_known():
    del data_dict[curren_word]
    next_card()
    new_data = {"French": {index: word for index, word in enumerate(data_dict.keys())},
                "English": {index: word for index, word in enumerate(data_dict.values())}}
    pd.DataFrame(new_data).to_csv("data/french_words_to_learn.csv", index=False)



# UI
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, print)

# flashcard sextion
image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")

flashcard = Canvas(width=800, height=526)
flashcard.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = flashcard.create_image(400, 263, image=image_front)

card_language = flashcard.create_text(400, 150, text="Title", font=FONT_1)
card_word = flashcard.create_text(400, 263, text="word", font=FONT_2)
flashcard.grid(column=0, row=0, columnspan=2)


# buttons section
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=next_card)
wrong_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, command=is_known)
correct_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

next_card()
window.mainloop()
