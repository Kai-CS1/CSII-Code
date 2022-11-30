'''
Created on Nov 14, 2022
@author: KHarashima25

This code allows the user to play a game of rock paper scissors against a computer playing pseudorandomly
No current bugs
Bonuses - Repeat Game option
'''
from random import randint                                          # for random computer move

def main():
    board = [['1','2','3'], ['4','5','6'], ['7','8','9']]           # set board to default
    printBoard(board)                                               # print clean board -> See printBoard for all future uses
    status = 2                                                      # set default (playing) status
    while status != 1 or status != 0 or status != 3:                # when the status is default, loop
        board = userChoice(board)                                   # allow the user to choose
        printBoard(board)                                           # print the board after the user chooses
        status = detectWin(board)                                   # detects a win on either side, or a tie -> See function detectWin
        if status == 0 or status == 1 or status == 3: break         # tests for a user win or tie
        print("--- Computer's Move ---")                            # seperater
        board = compChoice(board)                                   # generates a number for the computer and places it into the board
        printBoard(board)                                           # prints the board after the computer choice
        status = detectWin(board)                                   # detects a win on either side, or a tie -> See function detectWin
        if status == 0 or status == 1 or status == 3: break         # tests for a computer win or tie
    getResult(status)                                               # end program -> See function getResult

def printBoard(board): # takes the board list and prints the board
    for row in range(0,3):                                        
        column = 0
        for column in range(0,3): print(board[row][column],end = ' ')
        print('')

def userChoice(board): # takes the board, asks the user for an input, inputs their answer into the board, returns the new board       
    num = input('What number would you like to place in?\n')
    if num == '1' and board[0][0] == '1': board[0][0] = 'X'
    elif num == '2' and board[0][1] == '2': board[0][1] = 'X'
    elif num == '3' and board[0][2] == '3': board[0][2] = 'X'
    elif num == '4' and board[1][0] == '4': board[1][0] = 'X'
    elif num == '5' and board[1][1] == '5': board[1][1] = 'X'
    elif num == '6' and board[1][2] == '6': board[1][2] = 'X'
    elif num == '7' and board[2][0] == '7': board[2][0] = 'X'
    elif num == '8' and board[2][1] == '8': board[2][1] = 'X'
    elif num == '9' and board[2][2] == '9': board[2][2] = 'X'
    else:
        print("That spot is either already occupied, or your answer is not valid")
        board = userChoice(board)
    return board

def compChoice(board): # takes the board, generates a random number for the user, inputs into the board, returns the new board
    for _ in range(3): num = randint(1, 9)
    if num == 1 and board[0][0] == '1': board[0][0] = '0'
    elif num == 2 and board[0][1] == '2': board[0][1] = '0'
    elif num == 3 and board[0][2] == '3': board[0][2] = '0'
    elif num == 4 and board[1][0] == '4': board[1][0] = '0'
    elif num == 5 and board[1][1] == '5': board[1][1] = '0'
    elif num == 6 and board[1][2] == '6': board[1][2] = '0'
    elif num == 7 and board[2][0] == '7': board[2][0] = '0'
    elif num == 8 and board[2][1] == '8': board[2][1] = '0'
    elif num == 9 and board[2][2] == '9': board[2][2] = '0'
    else: board = compChoice(board)
    return board

def detectWin(board): # uses board - hardcoding for detecting a win on either side or a tie, returns status of game
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X' or board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X' or board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X' or board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X' or board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X': status= 0 
    elif board[0][0] == '0' and board[0][1] == '0' and board[0][2] == '0' or board[1][0] == '0' and board[1][1] == '0' and board[1][2] == '0' or board[2][0] == '0' and board[2][1] == '0' and board[2][2] == '0' or board[0][0] == '0' and board[1][0] == '0' and board[2][0] == '0' or board[0][1] == '0' and board[1][1] == '0' and board[2][1] == '0' or board[0][2] == '0' and board[1][2] == '0' and board[2][2] == '0' or board[0][0] == '0' and board[1][1] == '0' and board[2][2] == '0' or board[0][2] == '0' and board[1][1] == '0' and board[2][0] == '0': status= 1 
    elif board[0][0] == '1' or board[0][1] == '2' or board[0][2] == '3' or board[1][0] == '4' or board[1][1] == '5' or board[1][2] == '6' or board[2][0] == '7' or board[2][1] == '8' or board[2][2] == '9': status  =2
    else: status=3
    return status

def getResult(status): # prints the results of the game (using status) and offers a repeat
    if status== 0:print("You win!")
    elif status==1:print("The computer has won!")
    elif status==3:print("You are tied")
    passcodeinput = input("If you want to play again, type in \"Repeat Game\". If you don\'t, just type anything else\n")
    passcodeinput = passcodeinput.lower()
    if 'repeat' in passcodeinput:main()
    else:    exit()
if __name__ == '__main__': main()