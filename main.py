from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Place your bet",prompt="Pick a turtle from rainbow colors:\n"
                                                          " red, green,yellow, purple, orange or blue ").lower()
colors = ["red", "green", "yellow", "purple", "orange", "blue"]
position = -100
all_turtles = []

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    position += 40
    turtle.goto(x=-230, y=position)
    all_turtles.append(turtle)

game_over = False

while game_over == False:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            game_over = True
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The winner is {winner} turtle")
            else:
                print(f"You lost! The winner is {winner} turtle")
        distance = random.randint(0,10)
        turtle.forward(distance)



screen.exitonclick()