def get_question2 ():
    while True:
        answer = (input("Введите 2 числа от 1 до 100 через пробел - они будут диапазоном для угадывания ---> ")).split(" ")
        if checkStr(answer):
            correct = strTOint(answer)
            return correct
        else:
            print("Ты ввел неправильные значения. Попробуем еще раз.")


def checkStr (str):
    if len(str) != 2:
        return False
    for num in str:
        try:
            int(num)
        except:
            return False
        if int(num) > 100 or int(num) < 1:
            return False
    return True


def strTOint (answer):
    lst = []
    for num in answer:
        lst.append(int(num))
    return lst


import random
def get_goal(lst):
    goal = random.randint (lst[0], lst[1])
    return goal


def get_tries():
    while True:
        tries = input("Введите количество попыток, за которое Вы угадаете число ---> ")
        try:
            int(tries)
        except:
            print("Вы ввели неправлиьное значение. Попробуем еще раз.")
        else:
            return int(tries)

def get_guess(question, tries) :
    while True:
        guess = input("Угадай число от " + str(question[0]) + " до " + str(question[1]) + ". У тебя " + str(
            tries) + " попыток. --->>> ")
        try:
            int(guess)
        except:
            print("Вы ввели неправлиьное значение. Попробуем еще раз.")
        else:
            return int(guess)

def get_compare(guess, goal, tries_def, tries):
    if guess == goal:
        print("Ты угадал с " + str(tries_def - tries) + " попытки. Поздравляю, возьми пирожок!")
        return True
    elif tries == 0:
        print("Ты проиграл. Увы....")
        return False
    elif guess > goal:
        print("Ты указал число больше задуманного. Попробуй еще раз, у тебя осталось " + str(tries) + " попыток")
        return None
    elif guess < goal:
        print("Ты указал число мешьше задуманного. Попробуй еще раз, у тебя осталось " + str(tries) + " попыток")
        return None

def get_anotherGame ():
    while True:
        answer = input("Хотите сыграть еще раз? Введите Y/N ---> ")
        if answer.upper() == "Y":
            return True
        elif answer.upper() == "N":
            return False
        else:
            print("Ваш ответ" + answer + " не понятен. Попробуем еще раз")
