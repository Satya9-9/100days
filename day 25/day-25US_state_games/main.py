from turtle import Turtle, Screen
import pandas as pd

my_turtle = Turtle()
screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
my_turtle.shape(image)

# # This function will take the input and just print it
# def get_mouse_click_coor(x, y):
#     print(x, y)

# # This method will give the coordinates that goes inside our function
# # Then our function will print the coordinates
# Turtle.onscreenclick(get_mouse_click_coor)
# Turtle.mainloop()
# screen.exitonclick()

df = pd.read_csv("50_states.csv")
counts = len(df["state"])
list_of_states = df["state"].tolist()

user_entered_states = []

moveing = Turtle()
moveing.hideturtle()
moveing.penup()

cnt = 0
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(
        title="Guess the state",
        prompt="What's another state's name"
    ).title().strip()

    print(answer_state)

    if not df[df["state"] == answer_state].empty:
        cnt += 1
        answer = df[df["state"] == answer_state]
        user_entered_states.append(answer.state.item())

        coor_x = int(answer["x"].iloc[0])
        coor_y = int(answer["y"].iloc[0])
        coor = (answer.x.item(), answer.y.item())

        moveing.goto(coor)
        moveing.write(answer_state)

    elif counts == cnt:
        game_is_on = False

    elif answer_state == "Exit":
        missing_State = []
        for state in list_of_states:
            if state not in user_entered_states:
                missing_State.append(state)

        new_data = pd.DataFrame(missing_State)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False

# states to learn we will append it to the csv file
