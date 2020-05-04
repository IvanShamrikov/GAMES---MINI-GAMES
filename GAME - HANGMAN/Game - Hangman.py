
# ----------------------
#
# *** WELCOME TO "HANGMAN" GAME ***
#   Let's start programming
#
# ----------------------



def displayBoard(missedLetters, correctLetters, secretWord, alfabet_board, theme):
    print(hangnam_pics[len(missedLetters)])
    print("Тема:",  theme)

    # Показываем состояние угадываемого слова на сейчас
    for index in range(len(secretWord)):
        dashed_word = ""
        for char in secretWord:
            if char in correctLetters:
                dashed_word = dashed_word + char + " "
            else:
                dashed_word += "_ "
    print("Слово на доске: ", dashed_word)


    # Показываем остальные буквы, доступные к угадыванию
    for index in range (len(alfabet)):
        if alfabet[index] in correctLetters or alfabet[index] in missedLetters:
            alfabet_board += "_ "
        else:
            alfabet_board = alfabet_board + alfabet[index] + " "
    print("Оставшиеся буквы: ", alfabet_board)


    #Показываем список ошибочных букв
    print("Ошибочные буквы: ", end = "")
    if missedLetters == "":
        print(" -", end="")
    else:
        for letter in missedLetters:
            print(letter + " ", end="")
    print()




def getRandomWord(themes):
    theme = random.choice(tuple(themes.keys()))
    word = random.choice(themes[theme])
    word = word.upper()
    return theme, word


def getGuess(correctLetters, missedLetters):
    while True:
        print()
        guess = input("Введите букву --> ").upper()
        if len(guess) != 1:
            print("Пожалуйста, введите одну букву.")
        elif guess in correctLetters or guess in missedLetters:
            print("Вы уже называли эту букву")
        elif guess in (" _") or guess not in alfabet or type(guess) != str:
            print("Это не буква. Введите БУКВУ")
        else:
            break
    print()
    return guess


def gameFinish(correctLetters, missedLetters, secretWord):
    unikLettersInSecretWord = set()
    for i in secretWord:
        unikLettersInSecretWord.add(i)

    if len(correctLetters) == len(unikLettersInSecretWord):
        print()
        print()
        print(f'''                  ПОЗДРАВЛЯЕМ! 
    Вы угадали слово {secretWord} и выиграли игру "ВИСЕЛИЦА"!''')
        return True
    elif len(missedLetters) == 6:
        print()
        print()
        print(f'''                  ИГРА ОКОНЧЕНА! 
    Вы не угадали слово {secretWord} и програли в игру "ВИСЕЛИЦА"!''')
        return True
    else:
        return False

def oneMore():
    while True:
        print()
        answer = input("Хотите сыграть еще раз? Введите да/нет --->").lower()
        if answer == "да":
            print()
            print()
            print()
            print()
            return True
        elif answer == "нет":
            return False
        else:
            print("Ваш ответ не понятен. Попробуем еще раз.")






def mainGame(themes):
    missedLetters = ""
    correctLetters = ""
    alfabet_board = ""

    print()
    print(
        '''                         Добро пожаловать в игру ВИСЕЛИЦА!
        У Вас есть 6 попыток угадать слово по заданной теме.
        После каждой неверной попытки к рисунку будет добавляться часть человечка.
        Если слово будет угадано до того, как человечек станет виден полностью - Вы выиграли!
                                    Удачи!
        ''')
    print()
    input("Нажмите ENTER для старта.")
    #Выбираем секретное слово
    theme, secretWord = getRandomWord(themes)


    while True:
        #Показываем текущее состояние игры
        displayBoard(missedLetters , correctLetters, secretWord, alfabet_board, theme)

        #Проверка результатов Игры - пишется последним
        if gameFinish(correctLetters, missedLetters, secretWord):
            if oneMore():
                mainGame(themes)
            else:
                break

        #Запрос пользователю на введение буквы. Проверка буквы.
        guess = getGuess(correctLetters, missedLetters)

        #Сверка буквы и запись в соответствующий массив
        if guess in secretWord:
            print("Такая буква есть в слове!")
            correctLetters += guess
            time.sleep(2)
        else:
            print("Такой буквы нет в слове!")
            missedLetters += guess
            time.sleep(2)



import random
import time

hangnam_pics = [
    '''
    +---+
        |
        |
        |
       ===''',
    '''
   +---+
   O    |
        |
        |
       ===''',
    '''
   +---+
   O    |
   |    |
        |
       ===''',
    '''
   +---+
   O    |
   |\   |
        |
       ===''',
    '''
   +---+
   O    |
  /|\   |
        |
       ===''',
    '''   
   +---+
   O    |
  /|\   |
  /     |
       ===''',
    '''  
   +---+
   O    |
  /|\   |
  / \   |
       ==='''
   ]
alfabet = ["А","Б","В","Г","Д","Е","Ë","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф", "Х","Ч","Ц","Ч","Ш","Щ","Ь","Ъ","Ы","Э","Ю","Я"]
goroda = ["Киев", "Одесса", "Харьков", "Львов", "Николаев", "Житомир", "Полтава", "Чернигов"]
zhyvotnye = ["аист","акула","бабуин","баран", "тритон", "черепаха", "ястреб", "ящерица", "муравей","барсук","медведь", "медоед", "муравьед", "панда", "ленивец"]
themes = {"Города Украины": goroda, "Животные": zhyvotnye}

mainGame(themes)
print()
print("                 ВСЕГО ДОБРОГО!")
