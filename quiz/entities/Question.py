import random


class Question:
    def __init__(self, question, question_type):
        self.question = question
        self.type = question_type


class MultipleChoice(Question):
    def __init__(self, question, question_type, answers):
        super().__init__(question, question_type)
        self.answers = answers
        self.correctAnswer = answers[0]

    def get_answers(self):
        return random.shuffle(self.answers)

    def check_answer(self, answer):
        return answer == self.correctAnswer


class OpenQuestion(Question):
    pass
