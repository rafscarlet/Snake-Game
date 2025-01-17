import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__(shape='circle')
        self.penup()
        self.color('green')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed('fastest')
        self.relocate()
    
    def relocate(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
