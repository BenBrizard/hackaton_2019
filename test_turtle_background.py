from turtle import Screen, Turtle

WIDTH, HEIGHT = 900, 500

CURSOR_SIZE = 20

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor('blue')

background = Turtle('square', visible=False)
background.shapesize(HEIGHT/4 / CURSOR_SIZE, WIDTH / CURSOR_SIZE)
background.penup()
background.sety(-HEIGHT/2.5)
background.color('green')
background.stamp()

# your code here

screen.mainloop()
