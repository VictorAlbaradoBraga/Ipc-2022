import turtle

# Screen() method to get screen
wn = turtle.Screen()

# Creating tess object
tess = turtle.Turtle()


def triangle(x, y):
    # It is used to draw out the pen
    tess.penup()

    # It is used to move cursor at x and y position
    tess.goto(x, y)

    # It is used to draw in the pen
    tess.pendown()
    for i in range(3):
        # Move cursor 100 unit
        # Digit forward
        tess.forward(100)

        # Turn cursor 120 degree left
        tess.left(120)

        # Again,move cursor 100 unit
        # Digit forward
        tess.forward(100)


# Special built in function to send current
# Position of cursor to triangle
turtle.onscreenclick(triangle, 1)

turtle.listen()

# Hold the screen
turtle.done()
