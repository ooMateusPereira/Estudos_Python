import turtle

timmy = turtle.Turtle()
my_screen = turtle.Screen()

timmy.shape('turtle')
timmy.color('black')
timmy.fillcolor('coral')

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

print(my_screen.canvheight)
my_screen.exitonclick()
