from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)
bet = screen.textinput('Make a bet.', 'Choose a color turtle.')
colors = ['Red', 'Blue', 'Coral', 'Purple', 'Green', 'Yellow']
y_positions = [-70, -40, -10, 20, 50, 80]
race = False
all_turtles = []

if bet:
    race = True

for t in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[t])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_positions[t])
    all_turtles.append(new_turtle)

while race:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race = False
            winning_color = turtle.pencolor()
            
            if winning_color == bet:
                print(f"You've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! the {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()