# - Yellow -  Information with a general, but relative importance
# ? Orange -  Examples, abbreviations, acronyms, or explanations
# + Green -  Key words, proper nouns, dates, symbols or mathematical formulas
# ~ Blue -  Definitions of key words, or tabular data
# ! Pink - Important, relative to a test or my career
# * Purple -  Personal interest
# // Gray - Done


#! TODO 1 - TBD
#! TODO 2 - TBD
#! TODO 3 - TBD
#! TODO 4 - TBD
#! TODO 5 - TBD

# - establishing variables, immporting modules and setting up functions

import os
import random
import art
import var
import time
import turtle
import colorgram


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


# - the main program

clear_screen()
print(art.day)

tim.shape("circle")
tim.color("blue")
tim.fillcolor("purple")

tim.pensize(1)    # -  change the pen size
tim.hideturtle()  # -  make the "turle" invisible
tim.speed(10)     # -  pause for a moment

"""
pull out the colors using colorgram.py ✅
make a list of colors but in tuples ✅
found documenation at https://pypi.org/project/colorgram.py/ ✅
first, I had to install the package ✅


requirements...

1. 10 by 10 rows of spots ✅
2. each of dots 20 in size ✅
3. space them 50 apart ✅
4. put it in the middle ✅
5. clean it up ✅

"""


# - setting up import of colors from the image

rgb = []
col = colorgram.extract('image.jpg', 30)
for i in col:
    red = i.rgb.r
    blue = i.rgb.b
    green = i.rgb.g
    rgb.append((red, green, blue))

# - drawing the dots in rows and colummsn based on size and spacing

siz = 20
ste = 50
qua = 10

tim.penup()
i = int(qua / 2)

for y in range(-i, i):
    for x in range(-i, i):
        print(f"coordinates: {x}, {y}")
        tim.goto(x * ste, y * ste)
        tim.dot(siz, random.choice(rgb))


scr.exitonclick()
