# Prompt: write a simple python script to enable two players to play a game of tic-tac-toe
# temperature: 0.5
# Code generated by ChatGPT often does not work as expected. 
# This is because the model is trained on a large corpus of code, 
# but the code generated is not always correct. This is a limitation of the model, 
# and not a bug in the code. 

# Need to add createBoard function


#!/usr/bin/env python

import sys

def main():

    #create and initialize board

    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    #initialize player turn

    turn = 'X'

    #main game loop

    while True:

        #print board

        printBoard(board)

        #get player input

        row, col = getPlayerInput(turn)

        #update board

        updateBoard(board, row, col, turn)

        #check for winner

    if checkForWinner(board, turn):

        print (f'Player {turn}, wins!')

        sys.exit(0)

    #check for draw

    if checkForDraw(board):

        print ('It\'s a draw!')

        sys.exit(0)

    #switch turns

    if turn == 'X':

        turn = 'O'

    else:

        turn = 'X'

    def printBoard(board):

        print

    for i in range(3):

        for j in range(3):

            sys.stdout.write(board[i][j])

        if j != 2:

            sys.stdout.write('|')

        print

        if i != 2:

            print ('------')

            print

def getPlayerInput(turn):

    while True:

        print (f'Player {turn} \'s turn.')

        row = input('Enter row: ')

        col = input('Enter col: ')

        if row >= 0 and row <= 2 and col >= 0 and col <= 2 and board[row][col] == ' ':

            return row, col 

    else:

        print ('Invalid input. Please try again.')

def updateBoard(board, row, col, turn):

    board[row][col] = turn

def checkForWinner(board, turn):

    for i in range(3):

        if board[i][0] == turn and board[i][1] == turn and board[i][2] == turn:

            return True

        if board[0][i] == turn and board[1][i] == turn and board[2][i] == turn:

            return True

        if board[0][0] == turn and board[1][1] == turn and board[2][2] == turn:

            return True

        if board[0][2] == turn and board[1][1] == turn and board[2][0] == turn:

            return True

        return False

def checkForDraw(board):

    for i in range(3):

        for j in range(3):

            if board[i][j] == ' ':

                return False

        return True

if __name__ == '__main__':

    main()