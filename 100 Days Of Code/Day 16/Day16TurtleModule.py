import turtle

timmy = turtle.Turtle()
my_screen = turtle.Screen()
print(timmy)

timmy.forward(200)
timmy.left(120)
timmy.forward(300)
timmy.left(120)
timmy.forward(300)

timmy.shape('turtle')
timmy.color('black')
timmy.fillcolor('coral')
print(my_screen.canvheight)
my_screen.exitonclick()

