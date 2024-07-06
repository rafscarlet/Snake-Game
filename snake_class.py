from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
moving_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_pieces = []
        self.create_snake()
    
    def create_snake(self):
        for pos in positions:
            self.add_piece(pos)
    
    def add_piece(self, position):
        piece = Turtle(shape='square')
        piece.color('white')
        piece.penup()
        piece.goto(position)
        self.snake_pieces.append(piece)
    
    def extend(self):
        self.add_piece(self.snake_pieces[-1].pos())
    
    def move(self):
        for i in range(len(self.snake_pieces) - 1, 0, -1):
            new_x = self.snake_pieces[i - 1].xcor()
            new_y = self.snake_pieces[i - 1].ycor()
            self.snake_pieces[i].goto(new_x, new_y)
        self.snake_pieces[0].forward(distance=moving_distance)
    
    def reset(self):
        for piece in self.snake_pieces:
            piece.goto(1000, 1000)
        self.snake_pieces.clear()
        self.create_snake()
    
    def up(self):
        if self.snake_pieces[0].heading() != DOWN:
            self.snake_pieces[0].setheading(UP)
    
    def down(self):
        if self.snake_pieces[0].heading() != UP:
            self.snake_pieces[0].setheading(DOWN)
    
    def left(self):
        if self.snake_pieces[0].heading() != RIGHT:
            self.snake_pieces[0].setheading(LEFT)
    
    def right(self):
        if self.snake_pieces[0].heading() != LEFT:
            self.snake_pieces[0].setheading(RIGHT)
