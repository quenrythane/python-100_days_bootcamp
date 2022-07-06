from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = ("Arial", 48, "italic")
FONT_2 = ("Arial", 60, "bold")





# UI
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


# flashcard sextion
image_front = PhotoImage(file="images/card_front.png")
image_back = PhotoImage(file="images/card_back.png")

flashcard = Canvas(width=800, height=526)
flashcard.config(bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard.create_image(400, 263, image=image_front)

flashcard.create_text(400, 150, text="Title", font=FONT_1)
flashcard.create_text(400, 263, text="word", font=FONT_2)
flashcard.grid(column=0, row=0, columnspan=2)


# buttons section
wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=print)
wrong_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, command=print)
correct_button.config(highlightthickness=0, bg=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)

window.mainloop()
