from tkinter import *
from time import *
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        timer_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)

    elif reps % 8 == 0:
        timer_label.config(text= "Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)

    elif reps % 2 == 0:
        timer_label.config(text= "Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    clock_text = "{:02}:{:02}".format(count//60, count%60)
    canvas.itemconfig(timer_text, text=clock_text)
    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# highlightthickness hiding border between canvas and window
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN, highlightthickness=0)
timer_label.grid(column=1, row=0)

# start button
def start_clicked():
    pass

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# reset button
def reset_clicked():
    pass

reset_button = Button(text="Reset", command=reset_clicked, highlightthickness=0)
reset_button.grid(column=2, row=2)

# checks section
checks = "✔"
checks_label = Label(text=checks, fg=GREEN, bg=YELLOW)
checks_label.grid(column=1, row=3)


# .grid(column=0, row=3)
# .grid(column=2, row=3)


window.mainloop()
