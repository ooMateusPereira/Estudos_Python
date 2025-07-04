import turtle
import random

timmy = turtle.Turtle()
my_screen = turtle.Screen()
colours = ['Red', 'Blue', 'Coral', 'Purple', 'Green', 'Yellow']

def draw_shapes(n_sides):
    angle = 360 / n_sides
    for _ in range(n_sides):
        timmy.forward(100)
        timmy.right(angle)
    
for shape_shide in range(3, 11):
    timmy.color(random.choice(colours))
    draw_shapes(shape_shide)

print(my_screen.canvheight)
my_screen.exitonclick()