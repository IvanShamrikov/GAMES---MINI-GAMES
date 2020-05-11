# import random
#
# def drawBoard(board):
#     print('   |   |')
#     print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#     print('   |   |')
#     print('-----------')
#     print('   |   |')
#     print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#     print('   |   |')
#
#
# def inputPlayerLetter():
#     letter = ''
#     while not (letter == 'X' or letter == 'O'):
#         print('Do you want to be X or O?')
#         letter = input().upper()
#     if letter == 'X':
#         return ['X', 'O']
#     else:
#         return ['O', 'X']
#
# def whoGoesFirst():
#     if random.randint(0, 1) == 0:
#         return 'computer'
#     else:
#         return 'player'
#
# def playAgain():
#     print('Do you want to play again? (yes or no)')
#     return input().lower().startswith('y')
#
# def makeMove(board, letter, move):
#     board[move] = letter
#
# def isWinner(bo, le):
#     return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
#     (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
#     (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
#     (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
#     (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
#     (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
#     (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
#     (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
#
#
# def getBoardCopy(board):
# # Make a duplicate of the board list and return it the duplicate.
#     dupeBoard = []
#     for i in board:
#         dupeBoard.append(i)
#         return dupeBoard
#
# def isSpaceFree(board, move):
# # Return true if the passed move is free on the passed board.
#     return board[move] == ' '
#
# def getPlayerMove(board):
# # Let the player type in their move.
#     move = ' '
#     while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
#         print('What is your next move? (1-9)')
#     move = input()
#     return int(move)
#
# def chooseRandomMoveFromList(board, movesList):
# # Returns a valid move from the passed list on the passed board.
# # Returns None if there is no valid move.
#     possibleMoves = []
#     for i in movesList:
#         if isSpaceFree(board, i):
#             possibleMoves.append(i)
#
#     if len(possibleMoves) != 0:
#         return random.choice(possibleMoves)
#     else:
#         return None
#
# def getComputerMove(board, computerLetter):
# # Given a board and the computer's letter, determine where to move and return that move.
#     if computerLetter == 'X':
#         playerLetter = 'O'
#     else:
#         playerLetter = 'X'
#
# # Here is our algorithm for our Tic Tac Toe AI:
# # First, check if we can win in the next move
#     for i in range(1, 10):
#         copy = getBoardCopy(board)
#         if isSpaceFree(copy, i):
#             makeMove(copy, computerLetter, i)
#             if isWinner(copy, computerLetter):
#                 return i
#
# # Check if the player could win on their next move, and block them.
#     for i in range(1, 10):
#         copy = getBoardCopy(board)
#         if isSpaceFree(copy, i):
#             makeMove(copy, playerLetter, i)
#             if isWinner(copy, playerLetter):
#                 return i
#
# # Try to take one of the corners, if they are free.
#     move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
#     if move != None:
#         return move
#
# # Try to take the center, if it is free.
#
#     if isSpaceFree(board, 5):
#         return 5
#
# # Move on one of the sides.
#     return chooseRandomMoveFromList(board, [2, 4, 6, 8])
#
# def isBoardFull(board):
# # Return True if every space on the board has been taken. Otherwise return False.
#     for i in range(1, 10):
#         if isSpaceFree(board, i):
#             return False
#     return True
#
#
#
# print('Welcome to Tic Tac Toe!')
# while True:
# # Reset the board
#     theBoard = [' '] * 10
#     playerLetter, computerLetter = inputPlayerLetter()
#     turn = whoGoesFirst()
#     print('The ' + turn + ' will go first.')
#     gameIsPlaying = True
#
#     while gameIsPlaying:
#         if turn == 'player':
# # Player’s turn.
#             drawBoard(theBoard)
#             move = getPlayerMove(theBoard)
#             makeMove(theBoard, playerLetter, move)
#
#             if isWinner(theBoard, playerLetter):
#                 drawBoard(theBoard)
#                 print('Hooray! You have won the game!')
#                 gameIsPlaying = False
#             else:
#                 if isBoardFull(theBoard):
#                     drawBoard(theBoard)
#                     print('The game is a tie!')
#                     break
#                 else:
#                     turn = 'computer'
#         else:
# # Computer’s turn.
#             move = getComputerMove(theBoard, computerLetter)
#             makeMove(theBoard, computerLetter, move)
#             if isWinner(theBoard, computerLetter):
#                 drawBoard(theBoard)
#                 print('The computer has beaten you! You lose.')
#                 gameIsPlaying = False
#             else:
#                 if isBoardFull(theBoard):
#                     drawBoard(theBoard)
#                     print('The game is a tie!')
#                     break
#                 else:
#                     turn = 'player'
#
#
#
#     if not playAgain():
#         break
#

import random

def drawBoard(board):
    print(f'''
    | {board[7]} | {board[8]} | {board[9]} |
    + - + - + - +
    | {board[4]} | {board[5]} | {board[6]} |
    + - + - + - +
    | {board[1]} | {board[2]} | {board[3]} |
    ''')

def inputPlayerLetter():
    while True:
        answer = input("Please, choose X or O to play ---> ").upper()
        if answer !="X" and answer !="O":
            print('''
Something went wrong. Let's try again.
            ''')
        else:
            playerLetter = answer
            if playerLetter == "X":
                computerLetter = "O"
            else:
                computerLetter = "X"
            break
    return playerLetter, computerLetter


def whoGoesFirst():
    rand = random.randint(0,1)
    if rand == 0:
        return "Player"
    else:
        return "Computer"

def makeMove(board, letter, move):
    board[move]=letter

def isWinner(board,letter):
    a = board[1] == letter and board[2] == letter and board[3] == letter
    b = board[4] == letter and board[5] == letter and board[6] == letter
    c = board[7] == letter and board[8] == letter and board[9] == letter
    d = board[1] == letter and board[4] == letter and board[7] == letter
    e = board[2] == letter and board[5] == letter and board[8] == letter
    f = board[3] == letter and board[6] == letter and board[9] == letter
    h = board[1] == letter and board[5] == letter and board[9] == letter
    i = board[3] == letter and board[5] == letter and board[7] == letter
    return  a or b or c or d or e or f or h or i


def getPlayerMove(board):
    while True:
        move = input("Your next move? (1-9) ---> ")
        if move in ["1 2 3 4 5 6 7 8 9".split()] and board[move] != " ":
            print('''
Something went wrong. Let's try again.
''')
        else:
            return int(move)

def chooseRandomMove(board, moveList):
    listOfPossibleMoves = []
    for i in moveList:
        if board[i] == " ":
            listOfPossibleMoves.append(i)
    if len(listOfPossibleMoves) > 0:
        randomMove = random.choice(listOfPossibleMoves)
        return randomMove
    else:
        return None


def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    for i in range (1,10):
        boardCopy = getBoardCopy(board)
        if boardCopy[i] == " ":
            makeMove(boardCopy,computerLetter,i)
            if isWinner (boardCopy, computerLetter):
                return i

    for i in range (1,10):
        boardCopy = getBoardCopy(board)
        if boardCopy[i] == " ":
            makeMove(boardCopy,playerLetter,i)
            if isWinner (boardCopy, playerLetter):
                return i

    move = chooseRandomMove(board, [1,3,7,9])
    if move != None:
        return move

    if board[5] == " ":
        move = 5
        return move

    move = chooseRandomMove(board, [2,4,6,8])
    if move != None:
        return move

def isboardFull(board):
    for i in range (1,10):
        if board[i] == " ":
            return False
    return True

print(f'''
{"="*50}
                  TIC TAC TOE
{"="*50}
''')




gameIsOn = True
while gameIsOn:
    board = [" "]*10

    playerLetter, computerLetter = inputPlayerLetter()

    turn = whoGoesFirst()

    print(f"{turn} is moving first.")

    while True:
        if turn == "Player":
           drawBoard(board)
           move = getPlayerMove(board)
           makeMove(board, playerLetter, move)

           if isWinner(board,playerLetter):
               drawBoard(board)
               print("YOU WIN!!!")
               break
           else:
                if isboardFull(board):
                    print("There is no winners!")
                    break
                else:
                    turn = "Computer"

        elif turn == "Computer":
            move = getComputerMove(board, computerLetter)
            makeMove(board, computerLetter, move)

            if isWinner(board, computerLetter):
                drawBoard(board)
                print("COMPUTER WIN!!!")
                break
            else:
                if isboardFull(board):
                    print("There is no winners!")
                    break
                else:
                    turn = "Player"

    answer = ""
    while answer != "Y" or answer != "N":
        answer = input('''
Do you want to play another game? Type Y/N ---> ''')
        if answer.upper() == "Y":
            gameIsOn = True
            break
        elif answer.upper() == "N":
            gameIsOn = False
            break
        else:
            print('''
Something went wrong. Let's try again.
                        ''')

