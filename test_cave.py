from fonctions import *

############################################################################

# create the string of turtle instructions
instruction_string = create_l_system(5, "X")
print(instruction_string)

# setup for drawing
window = turtle.Screen()
greg = turtle.Turtle()
greg.speed(0)

# using screen.tracer() speeds up your drawing (by skipping some frames when drawing)
#window.tracer(10)

# move turtle to left side of screen
greg.up()
greg.back(200)
greg.down()

# draw the picture, using angle 60 and segment length 5
draw_l_system(greg, instruction_string, 22.5, 5)
input("Press Escape to continue...")
