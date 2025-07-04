import turtle

timmy = turtle.Turtle()
my_screen = turtle.Screen()

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

print(my_screen.canvheight)
my_screen.exitonclick()