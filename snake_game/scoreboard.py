from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):

        super().__init__()
        self.score = 0
        with open('data.txt',mode='r') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0,278)
        self.update_scroreboard()

    def update_scroreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_scroreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scroreboard()


