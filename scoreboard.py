from turtle import Turtle


ALIGNMENT = 'center'
FONT = ('Arial', 15, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as file:
            self.highscore = int(file.read())
        self.pu()
        self.goto(0, 270)
        self.color('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.highscore}')
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
