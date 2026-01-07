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


ALIGN = "center"  # - center the text
FONT = ("Courier", 16, "normal")  # - font for the text


# - define a class named Scoreboard

"""
1. create a class based on Turtle ✅
2. keep track of score ✅
3. display the score using turtle.write ✅
4. use the turtle.clear method to clear the screen ✅


"""


class ScoreBoard(turtle.Turtle):
    # ? Constructor method to initialize attributes
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.write(f"Score: {self.score} ", align=ALIGN,
                   font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGN,
                   font=FONT)
