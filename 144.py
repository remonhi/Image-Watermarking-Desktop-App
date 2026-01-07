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


BTW, it is possible to initilize the turtle shape 

1. prompt user for bet 
    a. ask for color ✅
    b. check to see if color is in the list 
        - need to look through some old code 
        - then, prompt on the Tcl/Tk screen

        
    
2. create 6 turtles ✅
    a. set the colors ✅
    b. initlaize each with a different color ✅
    c. then move them all to starting point ✅

3. run the race
    a. establish the finish line 
    b. move each turtle forward a random distance 
    c. check to see if any turtle has crossed the finish line (.xcor() > 0)
    d. if so, print the winner 
    
4. report status of the bet 


    







"""

# - setting up the screen

x = 500
y = 400
space = 20
scr.setup(width=x, height=y)

# - asking user for bet
bet = scr.textinput(title="Make your bet",
                    prompt="Which turtle will win the race? Enter a color: ")


# - creating 6 turtles

color = ["red", "orange", "yellow", "green", "blue",
         "indigo", "violet"]  # - the turtle names

turtles = []

for i in color:
    j = turtle.Turtle()  # - create a new turtle
    j.hideturtle()       # - make the "turle" invisible
    j.penup()            # - lift the pen up
    j.color(i)           # - set the color of the turtle
    j.shape("turtle")    # - set the shape of the turtle
    turtles.append(j)    # - add the turtle to the list


# - moving the turtles to starting point

x = int((x/2 - space) * -1)    # - set the left side of the screen
y = int((y/2 - (len(turtles) * space)/2))  # - set the top row for racer

for i in range(len(turtles)):
    print(f"coordinates: {x}, {y}")
    turtles[i].showturtle()     # -  show the turtle
    turtles[i].goto(x, y)       # -  move to the left side of the screen
    y = y - space * 2           # -  move down the screen


# - run the race


# - making sure screen doesn't close

scr.exitonclick()
