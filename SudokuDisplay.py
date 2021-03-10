from tkinter import *
from tkinter import ttk
import numpy as np
from SudokuBoard import SudokuBoard
from itertools import product
from time import sleep
from copy import copy



class SudokuDisplay:

    # Create window
    def __init__(self, board):
        # self.fenster = None
        self.board = board
        self.labelList = []

        # create window
        self.window = Tk()
        self.window.title("Sudoku Solver")

        # get current board
        current_board = self.board.get_board()

        # fill in the sudoku
        for x in range(11):
            xadd = int(x / 4)
            xlabel = []
            for y in range(11):
                yadd = int(y / 4)

                if not (x == 3 or x == 7 or y == 3 or y == 7):
                    # fill in color and text
                    if current_board[x - xadd][y - yadd] == 0:
                        text = StringVar()
                        text.set('-')
                        color = '#FFCFC9'
                        flag = 'open'
                    else:
                        text = StringVar()
                        text.set(current_board[x - xadd][y - yadd])
                        color = 'gray'
                        flag = 'start'

                    # create label
                    label = Label(
                        master=self.window,
                        bg=color,
                        textvariable=text)

                    # create grid
                    label.grid(
                        row=x,
                        column=y,
                        padx='5',
                        pady='5',
                        sticky='ew')

                    self.labelList.append([label, text, flag])

            # draw grid for sudoku
            for i in range(2):
                # vertical lines
                ttk.Separator(self.window, orient="vertical").grid(
                    column=3+(i*4),
                    row=0,
                    rowspan=11,
                    sticky='ns')

                # horizontal lines
                ttk.Separator(self.window, orient="horizontal").grid(
                    column=0,
                    row=3+(i*4),
                    columnspan=11,
                    sticky='ew')

        # create solve button
        solve_button = Button(
            self.window,
            text="Solve",
            command=self.solve_board)

        solve_button.grid(
            row=11,
            column=0,
            columnspan=3,
            padx='5',
            pady='5',)

        # create exit button
        exit_button = Button(
            self.window,
            text="Close",
            command=self.window.quit)

        exit_button.grid(
            row=11,
            column=8,
            columnspan=3,
            padx='5',
            pady='5',)

        # wait for user input
        self.window.mainloop()

    # solve sudoku
    def solve_board(self):

        nonzeros = np.count_nonzero(self.board.get_board())
        is_valid = self.solve(
            board=self.board.get_board(),
            entries=81-nonzeros)

        if is_valid:
            print('Ergebnis konnte gefunden werden.')
        else:
            print(
                'Es konnte kein Erbegnis gefunden werden. \n'
                'Das Sudoku ist nicht machbar.')

    def solve(self, board, entries):

        if entries == 0:
            return True

        for xIndex, yIndex in product(range(9), repeat=2):
            kasten = board[xIndex][yIndex]
            if kasten != 0:
                continue
            else:
                board_copy = copy(board)
                for test in range(1, 10):

                    # check the solution at given position
                    solution_check = SudokuDisplay.check_solution(
                        board_copy, xIndex, yIndex, test)

                    # assign the value
                    board_copy[xIndex][yIndex] = test

                    # set flag for value for display
                    self.labelList[xIndex*9+yIndex][2] = solution_check

                    # update brett
                    self.update_board(board_copy.flatten())

                    # update display
                    self.window.update()

                    if solution_check == 'correct' and self.solve(board_copy, entries - 1):
                        return True

                    # add sleep for displaying the solve solver
                    # sleep(0.00005)
                    board[xIndex][yIndex] = 0
                    self.labelList[xIndex*9+yIndex][2] = 'open'

                return False

    # check if solution is possible
    @staticmethod
    def check_solution(brett, xIndex, yIndex, solution):

        # check if number is already in x row or y column
        inX = np.any(brett[xIndex, :] == solution)
        inY = np.any(brett[:, yIndex] == solution)

        # check if number is in 3x3 box
        [xBox, yBox] = SudokuBoard.get_box_index(xIndex, yIndex)
        box = brett[xBox[0]:xBox[1]+1, yBox[0]:yBox[1]+1]
        inBox = np.any(box == np.ones(box.shape)*solution)

        if inX or inY or inBox:
            return 'incorrect'
        else:
            return 'correct'

    def update_board(self, brett):

        # input als flatten von dem board
        for i, [label, text, flag] in enumerate(self.labelList):

            # adjust value
            if brett[i] == 0:
                text.set('-')
            else:
                text.set(str(brett[i]))

            # adjust color
            if flag == 'start':
                label['bg'] = 'gray'
            elif flag == 'open':
                label['bg'] = '#FFCFC9'
            elif flag == 'correct':
                label['bg'] = '#D5E88F'
            elif flag == 'incorrect':
                label['bg'] = 'red'
