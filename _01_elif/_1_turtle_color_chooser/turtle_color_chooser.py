import random
import turtle
from tkinter import simpledialog


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


# ====================== DO NOT EDIT THE CODE ABOVE ===========================

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # TODO 1) Create a new Turtle
    bob = turtle.Turtle()
    bob.shape('turtle')
    #      2) Make the turtle draw a shape (this will take more than one line
    #         of code)
    #      3) Set the pen width to 10
    bob.pensize(10)
    for i in range(300):
    #      4) Ask the user what color pen they would like to draw with
        r = simpledialog.askstring('pen color', "What color pen do you want?")
    #      5) Use an if/else statement to set the pen color that the user
    #         requested
        if r == 'red':
            bob.pencolor('red')
            bob.pendown()
            for i in range(4):
                bob.forward(100)
                bob.right(90)
        elif r == 'blue':
            bob.pencolor('blue')
            bob.pendown()
            for i in range(4):
                bob.forward(100)
                bob.right(90)
        elif r == 'green':
            bob.pencolor('green')
            bob.pendown()
            for i in range(4):
                bob.forward(100)
                bob.right(90)


    #      6) If the user doesn't enter anything, choose a random color
        else:
            bob.pencolor(get_random_color())
            bob.pendown()
            for i in range(4):
                bob.forward(100)
                bob.right(90)
    #      7) Put a loop around your code so that you keep asking the user for
    #         more colors & drawing them
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
