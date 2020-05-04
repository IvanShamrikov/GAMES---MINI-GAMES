def game ():
    question = lib.get_question2()
    goal = lib.get_goal(question)
    tries_def = lib.get_tries ()
    tries = tries_def

    while tries !=0:
        guess = lib.get_guess (question, tries)

        tries -= 1

        if lib.get_compare(guess, goal, tries_def, tries) == True or False:
            break



import library
game ()
while True:
    if lib.get_anotherGame():
        game()
    else:
        print("Всего доброго!")
        break