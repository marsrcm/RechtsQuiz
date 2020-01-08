# small, useful, necessary functions
import random
import os
import csv
from definitions import get_project_root
from entities.Question import MultipleChoice
from entities.QuestionType import Type


# should at some point implement a more sensible algorithm
# for choosing the next random questiosn
def random_question(questions):
    return random.choice(questions)


# wait for user to press ENTER before continuing
def wait_for_input():
    print("\nBitte 'ENTER' drücken, um weiterzumachen")
    input()


# clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_questions():
    path = get_project_root() / 'resources/questions.CSV'
    # noinspection PyTypeChecker
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        questions = []
        for row in reader:
            question = row[0]
            qtype = Type.MultipleChoice if 'Multiple Choice' in row[-1] else Type.OpenEnded
            if qtype == Type.MultipleChoice:
                # only add answers that are not empty
                answers = [a for a in row[1:-1] if a]
                questions.append(MultipleChoice(question, qtype, answers))
        return questions
