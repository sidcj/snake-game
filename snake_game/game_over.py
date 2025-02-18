from turtle import Turtle


class Game_Over(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()

    def go(self):
        self.write("GAME OVER", False, align='center', font=('Arial', 24, 'bold'))
