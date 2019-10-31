import turtle

def apply_rules(letter):
    """Apply rules to an individual letter, and return the result."""
    # Rule 1
    if letter == 'F':
        new_string = 'FF'
    # Rule 2
    elif letter == 'X':
        new_string= 'F-[[X]+X]+F[+FX]-X'
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
    stack = []
    for task in instructions:
        some_turtle.pd()
        if task in ["F", "G", "R", "L"]:
            some_turtle.forward(distance)
        elif task == "f":
            some_turtle.pu()  # pen up - not drawing
            some_turtle.forward(distance)
        elif task == "+":
            some_turtle.right(angle)
        elif task == "-":
            some_turtle.left(angle)
        elif task == "[":
            stack.append((some_turtle.position(), some_turtle.heading()))
        elif task == "]":
            some_turtle.pu()  # pen up - not drawing
            position, heading = stack.pop()
            some_turtle.goto(position)
            some_turtle.setheading(heading)
