import pandas as pd
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)


timmy = Turtle()
timmy.shape(image)


data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()


corrects = 0
counter = 0


while counter <50:
    answer_state = screen.textinput(f"{corrects} of 50 states correct", "What is the state?").title()

    # If user wants to end program before:
    if answer_state == "Exit":
        break

    if answer_state in all_states:
        corrects += 1
        names = Turtle()
        names.hideturtle()
        names.penup()
        names.speed("fastest")
        state_data = data[data.state == answer_state]
        names.goto(int(state_data.x), int(state_data.y))
        names.write(answer_state)
        all_states.remove(answer_state)

    counter+=1


screen.exitonclick()