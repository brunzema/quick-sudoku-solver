# import numpy as np
from SudokuBoard import SudokuBoard
from SudokuDisplay import SudokuDisplay

# input sudoku as 9x9 with 0s as empty spaces
input_board = ['006309005',
               '003000472',
               '805010030',
               '000407690',
               '002901008',
               '401080000',
               '080000204',
               '060570100',
               '030060700']

if __name__ == "__main__":
    # init brett
    brett = SudokuBoard(input_board)

    # display window
    window = SudokuDisplay(brett)
