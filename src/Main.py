import utilities.functions as func


def main():
    # TODO: print introduction
    # initialize all questions read from csv
    questions = func.init_questions()
    print('Questions found: ' + str(len(questions)))
    running = True

    while running:
        question = func.random_question(questions)
        # create mapping from question answers to a, b, c, d
        answers = dict(zip(['a', 'b', 'c', 'd'], question.get_answers()))
        print(question.get_question() + "\n")
        for key in answers.keys():
            print(key + ') ' + answers[key])
        user_input = None
        while user_input not in answers.keys():
            user_input = input()
        if question.check_answer(answers[user_input.lower()]):
            print('\nGlückwunsch, deine Antwort war richtig')
            func.wait_for_input()
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
                    func.wait_for_input()
        # clear console screen
        func.clear()


if __name__ == "__main__":
    main()
