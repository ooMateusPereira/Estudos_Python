import turtle
import random

timmy = turtle.Turtle()
colours = ['Red', 'Blue', 'Coral', 'Purple', 'Green', 'Yellow']
my_screen = turtle.Screen()
directions = [0, 90, 180, 270]
timmy.pensize(13)
timmy.speed('fastest')

for _ in range(200):
    timmy.color(random.choice(colours))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

print(my_screen.canvheight)
my_screen.exitonclick()