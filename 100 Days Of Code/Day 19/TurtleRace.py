from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(500, 400)
bet = screen.textinput('Make a bet.', 'Choose a color turtle.')
colors = ['Red', 'Blue', 'Coral', 'Purple', 'Green', 'Yellow']
y_positions = [-70, -40, -10, 20, 50, 80]

for t in range(0, 6):
    tim = Turtle(shape='turtle')
    tim.color(colors[t])
    tim.penup()
    tim.goto(x=-230, y=y_positions[t])




screen.exitonclick()