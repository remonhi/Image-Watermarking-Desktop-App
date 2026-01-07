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
import time       # - for time functions
import turtle     # - for turtle (the old Tcl/Tk) graphics
import art        # - for ASCII art


scr = turtle.Screen()  # - pull up screen class from turtle module


def clear_screen():
    if os.name == 'nt':  # 'nt' stands for Windows
        os.system('cls')
    else:  # For macOS and Linux (posix-based systems)
        os.system('clear')


# - the main program
clear_screen()  # - text based

day = "Day 20"
nam = os.path.basename(__file__)
nam = nam.replace(".py", "")
day = day + " - " + nam
print(art.text2art(day, font='medium'))


"""
notes...

Screen setup and creating snake body

1. do normal imports ✅
2. seutp screen as 600 x 600 ✅
3. change screen color and set title ✅
4. 


    







"""

# - setting up the screen

x = 600
y = 600
size = 20
scr.setup(width=x, height=y)
scr.bgcolor("black")
scr.title(day)


# - TODO 1. Create a snake body

snake = []

for i in range(0, 3):
    j = turtle.Turtle(shape="square")  # - create a new turtle
    j.hideturtle()       # - make the "turle" invisible
    j.penup()            # - lift the pen up
    j.color("white")     # - set the color of the turtle
    snake.append(j)      # - add the turtle to the list

x = 0
y = 0

for i in range(len(snake)):
    print(f"coordinates: {x}, {y}")
    snake[i].showturtle()     # -  show the turtle
    snake[i].goto(x, y)       # -  move to the left side of the screen
    x = x - size              # -  move down the screen


#! TODO 2. Move the snake


#! TODO 3. Control the snake
#! TODO 4. Detect collision with food
#! TODO 5. Create a scoreboard
#! TODO 6. Detect collision with wall
#! TODO 7. Detect collision with tail


# - run the race


# - making sure screen doesn't close

scr.exitonclick()
