import random

class Question:
    def __init__(self, question, question_type):
        self.question = question
        self.type = question_type

    def get_question(self):
        return self.question

    def __str__(self):
        return '<' + str(self.type) + ' Question ' + self.question + '>'


class MultipleChoice(Question):
    def __init__(self, question, question_type, answers):
        super().__init__(question, question_type)
        self.answers = answers
        self.correctAnswer = answers[0]

    def get_answers(self):
        return random.sample(self.answers, len(self.answers))

    def get_correct_answer(self):
        return self.correctAnswer

    def check_answer(self, answer):
        return answer == self.correctAnswer

    def __str__(self):
        return ('<' + str(self.type) + ' Question: ' + self.question + '; answers: ' + str(self.answers) + '; correct: '
                + self.correctAnswer + '>')


class OpenQuestion(Question):
    pass
