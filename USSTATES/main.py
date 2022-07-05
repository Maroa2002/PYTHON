import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
# converts the state column in the csv file to a list and assigns the list to a variable
all_states = data.state.to_list()
# creates a prompt for the user to input a guess and assigns the guess to a variable
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
print(answer_state)

# Check if the guess is among the 50 states
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(state_data.state.item())


screen.exitonclick()