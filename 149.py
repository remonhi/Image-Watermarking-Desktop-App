
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
from snake import Snake, clear_screen      # - from Day 20

# - the main program

clear_screen()  # - text based
day = "Day 20"
nam = os.path.basename(__file__)
nam = nam.replace(".py", "")
day = day + " - " + nam
print(art.text2art(day, font='medium'))

# - setting up the screen

scr = turtle.Screen()  # - pull up screen class from turtle module
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title(day)
scr.tracer(0)  # - turning off the annimation

# - TODO 1. Create a snake body

s = Snake()
scr.update()

# -  TODO 2. Move the snake

game_on = True
while game_on:
    s.move()
    time.sleep(1)
    scr.update()


#! TODO 3. Control the snake

#! TODO 4. Detect collision with food
#! TODO 5. Create a scoreboard
#! TODO 6. Detect collision with wall
#! TODO 7. Detect collision with tail


# - run the race


# - making sure screen doesn't close

scr.exitonclick()
