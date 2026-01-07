# - Yellow -  Information with a general, but relative importance
# ? Orange -  Examples, abbreviations, acronyms, or explanations
# + Green -  Key words, proper nouns, dates, symbols or mathematical formulas
# ~ Blue -  Definitions of key words, or tabular data
# ! Pink - Important, relative to a test or my career
# * Purple -  Personal interest
# // Gray - Done

# - establishing variables, immporting modules and setting up functions

import os         # - for OS commands to clear the screen
import random     # - for random number generation
import art        # - my personal collection of ASCII art
import var        # - my personal collection of variables and functions
import time       # - for time functions
import turtle     # - for turtle (the old Tcl/Tk) graphics
import art        # - for ASCII art


scr = turtle.Screen()  # - pull up screen class from turtle module
tim = turtle.Turtle()  # - pull up turtle class from turtle module
turtle.colormode(255)  # -  set the color mode to RGB


def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # For macOS and Linux (posix-based systems)
        os.system('clear')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def move_forward():
    tim.forward(10)


def W():
    tim.forward(10)


def S():
    tim.backward(10)


def A():
    tim.left(10)


def D():
    tim.right(10)


def C():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# - the main program
clear_screen()  # - text based

day = "Day 19"
nam = os.path.basename(__file__)
nam = nam.replace(".py", "")
day = day + " - " + nam
print(art.text2art(day, font='medium'))

tim.shape("arrow")
tim.color("black")
tim.pen(fillcolor="black", pencolor="blue", pensize=1)
tim.speed(10)

"""

notes...



requirements...
W key to go forward
S key to go backward
A key to go counter-clockwise
D key to go clockwise
C key to clear the screen

So I'm thinkng...

1. figure out how to make the keys work ✔️
2. figure out how to make the turtle move ✔️
3. clear the screen and go home ✔️






"""

# - moving the pen for game...interseting, don't need a loop becuase of pen controls

scr.listen()       # -  listen for key presses

scr.onkey(W, "w")  # -  move forward
scr.onkey(S, "s")  # -  move backward
scr.onkey(A, "a")  # -  move left
scr.onkey(D, "d")  # -  move right
scr.onkey(C, "c")  # -  clear the screen

scr.exitonclick()  # -  making sure screen doesn't close
