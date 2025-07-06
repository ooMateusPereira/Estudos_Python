import turtle

tim = turtle.Turtle()
my_screen = turtle.Screen()

def move_up():
    tim.forward(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

my_screen.listen()
my_screen.onkeypress(move_up, 'w')
my_screen.onkeypress(move_right, 'd')
my_screen.onkeypress(move_left, 'a')

print(my_screen.canvheight)
my_screen.exitonclick()