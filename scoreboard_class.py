from turtle import Turtle

FONTSTYLE = ("Courier", 22, "normal")
POSITION = (0, 270)
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color('white')
        self.penup()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.update()
    
    def increase(self):
        self.score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.goto(POSITION)
        self.write(arg=f"Score: {self.score} - Highscore: {self.highscore}", align=ALIGNMENT, font=FONTSTYLE)
    
    def game_over(self):
        self.update()
        self.home()
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONTSTYLE)
        self.reset_score()
    
    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

