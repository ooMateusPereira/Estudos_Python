import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
my_screen = t.Screen()
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_gap)

draw_spirograph(3)

print(my_screen.canvheight)
my_screen.exitonclick()