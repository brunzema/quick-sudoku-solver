import numpy as np


class SudokuBoard:

    def __init__(self, input_board):
        self.input_board = input_board
        self.board = []
        self.start_board = []

    def get_board(self):

        if len(self.board) == 0:

            for brett in self.input_board:
                row = [int(char) for char in brett]
                self.board.append(row)

            self.board = np.asarray(self.board)
            # assign start brett
            if not self.start_board:
                self.start_board = self.board

        return self.board

    @staticmethod
    def get_box_index(x_index, y_index):
        if x_index < 3:
            # x=1:3, y=1:3
            if y_index < 3:
                return [[0, 2], [0, 2]]
            # x=1:3, y=4:6
            elif 3 <= y_index < 6:
                return [[0, 2], [3, 5]]
            # x=1:3, y=7:9
            elif 6 <= y_index < 9:
                return [[0, 2], [6, 8]]
            else:
                print('Y-Index out of range.')
                return [[], []]

        elif 3 <= x_index < 6:
            # x=4:6, y=1:3
            if y_index < 3:
                return [[3, 5], [0, 2]]
            # x=4:6, y=4:6
            elif 3 <= y_index < 6:
                return [[3, 5], [3, 5]]
            # x=4:6, y=7:9
            elif 6 <= y_index < 9:
                return [[3, 5], [6, 8]]
            else:
                print('Y-Index out of range.')
                return [[], []]

        elif 6 <= x_index < 9:
            # x=7:9, y=1:3
            if y_index < 3:
                return [[6, 8], [0, 2]]
            # x=7:9, y=4:6
            elif 3 <= y_index < 6:
                return [[6, 8], [3, 5]]
            # x=7:9, y=7:9
            elif 6 <= y_index < 9:
                return [[6, 8], [6, 8]]
            else:
                print('Y-Index out of range.')
                return [[], []]

        else:
            print('X-Index out of range.')
            return [[], []]
