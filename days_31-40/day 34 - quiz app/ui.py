from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # score
        self.score_label = Label(self.window, text=f"Score: {0}", font=("Arial", 10), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # main frame
        self.canvas = Canvas(self.window, width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Quiz App",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR)

        # true button
        true_photo = PhotoImage(file="images/true.png")
        self.button_true = Button(self.window, command=self.pressed_true, image=true_photo)
        self.button_true.grid(row=2, column=0, padx=20)

        # false button
        false_photo = PhotoImage(file="images/false.png")
        self.button_false = Button(self.window, command=self.pressed_false, image=false_photo, padx=20, pady=20)
        self.button_false.grid(row=2, column=1, padx=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz")
            self.button_true.config(state=DISABLED)
            self.button_false.config(state=DISABLED)

    def pressed_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def pressed_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")

        self.canvas.after(1000, self.get_next_question)
