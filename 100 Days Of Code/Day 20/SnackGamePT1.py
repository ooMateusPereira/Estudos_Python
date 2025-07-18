from turtle import Turtle, Screen, exitonclick

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')

starting_positions = [(0,0), (-20,0), (-40,0)]

for position in starting_positions:
    new_segmente = Turtle('square')
    new_segmente.color('white')
    new_segmente.goto(position)


print(screen.canvheight)
screen.exitonclick()