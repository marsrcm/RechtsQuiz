from utilities.functions import init_questions, random_question, wait_for_input, clear

# TODO: print introduction
# initialize all questions read from csv
questions = init_questions()
print('Questions found: ' + str(len(questions)))
running = True

while running:
    question = random_question(questions)
    # create mapping from question answers to a, b, c, d
    answer_keys = ['a', 'b', 'c', 'd']
    answers = dict(zip(answer_keys, question.get_answers()))
    print(question.get_question() + "\n")
    for key in answers.keys():
        print(key + ') ' + answers[key])
    user_input = None
    while user_input not in answer_keys:
        user_input = input()
    if question.check_answer(answers[user_input.lower()]):
        print('\nGlückwunsch, deine Antwort war richtig')
        wait_for_input()
    else:
        print('\nLeider war diese Antwort falsch')
        print("'help' eingeben, um die korrekte Antwort anzuzeigen\n"
              "Alternativ einfach 'ENTER' drücken, um weiterzumachen")
        # TODO: I wonder if reusing this variable is the best idea
        while user_input.lower() != 'help' and user_input != '':
            user_input = input()
            if user_input.lower() == 'help':
                print('\nKORREKTE ANTWORT:')
                print(question.get_correct_answer())
                wait_for_input()
    # clear console screen
    clear()
