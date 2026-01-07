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
# import var        # - my personal collection of variables and functions
import time       # - for time functions
import turtle     # - for turtle (the old Tcl/Tk) graphics
import art    # - for ASCII art


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


# - the main program

clear_screen()
day = "Day 19"
nam = os.path.basename(__file__)
nam = nam.replace(".py", "")
day = day + " - " + nam
print(art.text2art(day, font='medium'))

tim.shape("circle")
tim.color("blue")
tim.fillcolor("purple")

tim.pensize(5)    # -  change the pen size
tim.speed(10)     # -  pause for a moment

"""

notes...



requirements...


"""

# - controlling turle with input (and a function as input)

scr.listen()                       # -  listen for key presses
scr.onkey(move_forward, "space")   # -  move forward
scr.exitonclick()                  # -  making sure screen doesn't close
