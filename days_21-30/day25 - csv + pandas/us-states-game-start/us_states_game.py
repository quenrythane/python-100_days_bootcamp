from turtle import *
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)  # this line couldn't be above screen.addshape()


# get coordinates from mouse click
def get_mouse_click_coordinates(x, y):
    print(x, y)
# onscreenclick(get_mouse_click_coordinates)


data = pd.read_csv("50_states.csv")
all_states = list(data["state"])
correct_states = []

while len(correct_states) < len(all_states):
    user_answer = textinput(f"{len(correct_states)}/50 States Correct", "What`s another state name").capitalize()

    if user_answer.lower() == "exit":
        states_to_learn_dict = {"states": [state for state in all_states if state not in correct_states]}
        df_to_learn = pd.DataFrame(states_to_learn_dict)
        df_to_learn.to_csv("states_to_learn.csv")
        break

    if user_answer in all_states and user_answer not in correct_states:
        correct_states.append(user_answer)
        state_data = data[data["state"] == user_answer]
        t = Turtle()
        t.hideturtle()
        t.penup()
        t.setposition(int(state_data["x"]),
                      int(state_data["y"]))
        t.write(user_answer)

screen.mainloop()
