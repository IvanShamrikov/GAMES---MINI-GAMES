def game ():
    question = Library.get_question2()
    goal = Library.get_goal(question)
    tries_def = Library.get_tries ()
    tries = tries_def

    while tries !=0:
        guess = Library.get_guess (question, tries)

        tries -= 1

        if Library.get_compare(guess, goal, tries_def, tries) == True or False:
            break



import Library
game ()
while True:
    if Library.get_anotherGame():
        game()
    else:
        print("Всего доброго!")
        break