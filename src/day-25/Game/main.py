import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="Whats another state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_csv = pandas.DataFrame(missing_states)
        new_csv.to_csv("missing_states.csv")
        break

    if answer_state in states:
        guessed_states.append(answer_state)
        state_row = data[data.state == answer_state]
        x_cor = int(state_row.x)
        y_cor = int(state_row.y)
        state_name = state_row.state.item()
        state = State(x_cor=x_cor, y_cor=y_cor, state_name=state_name)

# states to learn CSV
