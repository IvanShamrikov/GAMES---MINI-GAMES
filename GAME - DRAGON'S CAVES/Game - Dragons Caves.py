import random
import time

def displayIntro():
    print(
        '''Вы находитесь в землях, заселёнными Драконами.
Перед собой Вы видите 2 пещеры.
В одной из них - дружелюбный дракон,
который готов поделиться с Вами сокровищем.
Во второй - жадный и голодный дракон, который мигом Вас съест.''')
    print()

def chooseCave():
    cave = ""
    while cave != "1" or cave !="2":
        print("В какую пещеру Вы войдёте (введите 1 или 2) ---> ")
        cave = input()

    return cave

def checkCave(caveNumber):
    print("Вы приближаетесь к пещере...")
    time.sleep(2)
    print("Её темнота заставляет Вас дрожать от страха...")
    time.sleep(2)
    print("Большой Дракон выпрыгивает перед Вами! Он раскрывает свою пасть и...")
    time.sleep(2)

    friendlyCave = str(random.randint(1,2))

    if caveNumber == friendlyCave:
        print("... делится с Вами сокровищами.")
    else:
        print("... моментально Вас съедает")


playAgain = "да"
while playAgain == "да":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Хотите сыграть еще раз? (да или нет) --->")
    playAgain = input()