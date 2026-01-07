# - Yellow -  Information with a general, but relative importance
# ? Orange -  Examples, abbreviations, acronyms, or explanations
# + Green -  Key words, proper nouns, dates, symbols or mathematical formulas
# ~ Blue -  Definitions of key words, or tabular data
# ! Pink - Important, relative to a test or my career
# * Purple -  Personal interest
# // Gray - Done


from turtle import Turtle
import random

B = 260  # - set the boundary for the snake


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-B, B)
        random_y = random.randint(-B, B)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-B, B)
        random_y = random.randint(-B, B)
        self.goto(random_x, random_y)
