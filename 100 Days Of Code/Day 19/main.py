import turtle

tim = turtle.Turtle()
my_screen = turtle.Screen()
tim.speed('fastest')

def move():
    tim.forward(10)

def move_back():
    tim.forward(-10)

def move_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()

my_screen.listen()
my_screen.onkeypress(move, 'w')
my_screen.onkeypress(move_back, 's')
my_screen.onkeypress(move_right, 'd')
my_screen.onkeypress(move_left, 'a')
my_screen.onkeypress(clear, 'c')

print(my_screen.canvheight)
my_screen.exitonclick()