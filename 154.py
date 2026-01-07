
"""
notes...

"""

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
import time       # - for time funcdtions
import snake      # - Snake class from day 20
import food       # - Food class from day 21


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

# - setting up the screen

c = turtle.Screen()  # - pull up screen class from turtle module
c.setup(width=600, height=600)
c.bgcolor("black")
c.title(day)
c.tracer(0)  # - turning off the annimation

# - create a snake body & food

s = snake.Snake()
f = food.Food()
c.update()
c.listen()
c.onkey(s.up, "Up")
c.onkey(s.down, "Down")
c.onkey(s.left, "Left")
c.onkey(s.right, "Right")

# -  loop it and play the game

game_on = True
while game_on:
    s.move()
    time.sleep(0.5)
    c.update()

    #! detect collision with food
    # ? see documentaion for Turtle.distance that show a Turtle object instance can be used
    if s.head.distance(f) < 15:
        f.refresh()

        # # - add a segment
        # new_segment = turtle.Turtle()
        # new_segment.shape("square")
        # new_segment.color("white")
        # new_segment.penup()
        # s.seg.append(new_segment)


# - making sure screen doesn't close

c.exitonclick()
