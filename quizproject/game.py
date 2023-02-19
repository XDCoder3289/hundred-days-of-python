from data import question_data

class Game:
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.num = 0
    def generate_rando(self):
        self.question = question_data[self.num]['text'].lower()
        self.correct_ans = question_data[self.num]['answer'].lower()
        return [self.question, self.correct_ans]