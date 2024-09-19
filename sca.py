import random

def drawBoard(Board):
    print(f'''
{Board[7]} | {Board[8]} | {Board[9]} 
{Board[4]} | {Board[5]} | {Board[6]} 
{Board[1]} | {Board[2]} | {Board[3]}''')

def whoGoesFirst():
    if random.randint(0,1) == 0:
    # if random.randit() == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
    return (
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[1] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le)
    )

def GetboardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
        return boardCopy

def isSpaceFree(board, move):
    return board[move] == ' '

def GetPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('what is the next move? (1-9)')
        move = input()
    return int(move)

def ChooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
            if len(possibleMoves) != 0:
                return random.choice(possibleMoves)
            else:
                return None

def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = '0'
    else:
        playerLetter = 'X'

    for i in range(1, 10):
        boardCopy = GetboardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = GetboardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy,playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = ChooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if isSpaceFree(board, 5):
        return 5
    return ChooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def InputplayerLetter():
    letter = ''
    while not (letter == 'X' or letter == '0'):
        print('Do you want to be X or 0?')
        letter = input().upper()
    if letter == 'X':
        return ['X', '0']
    else:
        return ['0', 'X']

# def drawBoard(Board):
    # print(f'{Board[7]} | {Board[8]} | {Board[9]}')
    # print('-+-+-')
    # print(f'{Board[4]} | {Board[5]} | {Board[6]}')
    # print('-+-+-')
    # print(f'{Board[1]} | {Board[2]} | {Board[3]}')
    # print(f'''{Board[7]} | {Board[8]} | {Board[9]}'
    # '-+-+-'
    # '{Board[4]} | {Board[5]} | {Board[6]}'
    # '-+-+-'
    # '{Board[1]} | {Board[2]} | {Board[3]}''')


def main():
    print('welcome to Tic-Tak-Toe')
    while True:
        theBoard = [' '] * 10
        playerLetter, computerLetter = InputplayerLetter()
        turn = whoGoesFirst()
        print(f'the {turn} will go first')
        gameIsPlaying = True
        while gameIsPlaying:
            if turn == 'player':
                drawBoard(theBoard)
                move = GetPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('hooray? you have won the game')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('the game is a tie')
                        break
                    else:
                        turn = 'computer'
            else:
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)
                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('you lose')
                    gameIsPlaying = False
                else:
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('game is tie')
                        break
                    else:
                        turn = 'player'
        print('do you want to play again?(yes/no)')
        if not input().lower().startswith('y'):
            break

if __name__ == '__main__':
    main()