import turtle

def apply_rules(letter):
    """Apply rules to an individual letter, and return the result."""
    # Rule 1
    if letter == 'F':
        new_string = 'X'
        
    elif letter == 'X':
        new_string = 'F-[[X]-1X]+2F-[+3FX]+1X'

    # no rules apply so keep the character
    else:
        new_string = letter

    return new_string


def process_string(original_string):
    """Apply rules to a string, one letter at a time, and return the result."""
    tranformed_string = ""
    for letter in original_string:
        tranformed_string = tranformed_string + apply_rules(letter)

    return tranformed_string

def create_l_system(number_of_iterations, axiom):
    """Begin with an axiom, and apply rules to the original axiom string number_of_iterations times, then return the result."""
    start_string = axiom
    for counter in range(number_of_iterations):
        end_string = process_string(start_string)
        start_string = end_string

    return end_string

def draw_l_system(some_turtle, instructions, angle, distance):
    """Draw with some_turtle, interpreting each letter in the instructions passed in."""
    for task in instructions:
        if task == 'F':
            some_turtle.forward(distance)
        elif task == 'B':
            some_turtle.backward(distance)
        elif task == '+':
            some_turtle.right(angle)
        elif task == '-':
            some_turtle.left(angle)

############################################################################

# create the string of turtle instructions
instruction_string = create_l_system(4, "X")
print(instruction_string)

# setup for drawing
window = turtle.Screen()
jill = turtle.Turtle()
jill.speed(0)

# using screen.tracer() speeds up your drawing (by skipping some frames when drawing)
#window.tracer(10)

# move turtle to left side of screen
jill.up()
jill.back(200)
jill.down()


# draw the picture, using angle 60 and segment length 5
draw_l_system(jill, instruction_string,25, 5)

turtle.done()
turtle.bye()