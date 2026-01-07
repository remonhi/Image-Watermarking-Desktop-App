
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

import os          # - for OS commands to clear the screen
import random      # - for random number generation
import time        # - for time functions
import turtle      # - for turtle (the old Tcl/Tk) graphics
import art         # - for ASCII art
import time        # - for time funcdtions
import snake       # - Snake class from day 20
import food        # - Food class from day 21
import scoreboard  # - Scoreboard class from day 22

SCREEN_SIZE = 600  # - set the screen size
BOUNDARY = abs(SCREEN_SIZE)/2 - 20  # - set the boundary for the snake


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
c.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
c.bgcolor("black")
c.title(day)
c.tracer(0)  # - turning off the annimation

# - create a snake body & food

s = snake.Snake()
f = food.Food()
b = scoreboard.ScoreBoard()

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
    time.sleep(0.3)
    c.update()

    # - module 154 | detect collision with food
    # ? see documentaion for Turtle.distance that show a Turtle object instance can be used
    if s.head.distance(f) < 15:
        f.refresh()
        s.extend()
        b.update()

    # -  module 156 | detect collision with wall
    if s.head.xcor() > BOUNDARY or s.head.xcor() < -BOUNDARY or s.head.ycor() > BOUNDARY or s.head.ycor() < -BOUNDARY:
        game_on = False
        b.goto(0, 0)
        b.write("GAME OVER", align="center", font=("Courier", 16, "normal"))

    #! - module 157 | detect collision with tail
    for m in s.seg:
        if m == s.head:
            pass
        elif s.head.distance(m) < 10:
            game_on = False
            b.goto(0, 0)
            b.write("GAME OVER", align="center",
                    font=("Courier", 16, "normal"))


# - making sure screen doesn't close

c.exitonclick()
