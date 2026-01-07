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


turtle_colors = [
    "red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan",
    "magenta", "brown", "black", "white", "gray", "gold", "silver",
    "darkblue", "lightgreen", "tomato", "lavender", "peachpuff",
    "deepskyblue", "forestgreen", "lightsalmon"
]


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


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


# - define a class named Snake
class Snake:
    # Constructor method to initialize attributes
    def __init__(self):
        # self.name = name  # Instance variable for name
        # self.age = age    # Instance variable for age
        self.x = 0
        self.y = 0
        self.size = 20
        self.seg = []
        self.create()
        self.head = self.seg[0]

    def create(self):

        print("debug create snake")

        for i in range(0, 3):
            j = turtle.Turtle(shape="square")  # - create a new turtle
            j.hideturtle()       # - make the "turle" invisible
            j.penup()            # - lift the pen up
            j.color("white")     # - set the color of the turtle
            self.seg.append(j)      # - add the turtle to the list

        for i in range(len(self.seg)):
            print(f"coordinates: {self.x}, {self.y}")
            self.seg[i].showturtle()     # -  show the turtle
            self.seg[i].penup()          # - hide the pen
            self.seg[i].goto(self.x, self.y)
            self.x = self.x - self.size              # -  move down the screen

        #! TODO 2. Move the snake

    def move(self):
        for i in range(len(self.seg)-1, 0, -1):
            new_x = self.seg[i-1].xcor()
            new_y = self.seg[i-1].ycor()
            self.seg[i].goto(new_x, new_y)
        self.seg[0].forward(self.size)

    def up(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):  # good
        print(f"heading: {self.head.heading()}")
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        j = turtle.Turtle(shape="square")
        j.hideturtle()
        j.penup()
        j.color(random.choice(turtle_colors))
        self.seg.append(j)
        i = len(self.seg) - 1
        x = self.seg[i-1].xcor()
        y = self.seg[i-1].ycor()
        self.seg[i].goto(x, y)
        self.seg[i].showturtle()
