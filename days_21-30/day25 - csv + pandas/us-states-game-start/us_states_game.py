from turtle import Screen, shape

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image) # this line couldn't be above screen.addshape()



screen.exitonclick()
