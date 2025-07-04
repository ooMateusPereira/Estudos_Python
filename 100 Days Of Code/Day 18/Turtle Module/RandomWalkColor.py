import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

my_screen = turtle.Screen()
directions = [0, 90, 180, 270]
timmy.pensize(13)
timmy.speed('fastest')

for _ in range(200):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

print(my_screen.canvheight)
my_screen.exitonclick()