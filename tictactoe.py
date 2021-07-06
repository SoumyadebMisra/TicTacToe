import math
import random
import time


class Game:
    def __init__(self):
        self.board = self.make_board()

    @staticmethod
    def make_board():
        return ['  ' for i in range(9)]

    def print_board(self):
        for row in [self.board[i * 3: (i + 1) * 3] for i in range(3)]:
            print('|' + '|'.join(row) + '|')
            print('-----------')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')
            print('-------------')

    def get_move(self, letter):
        move = input('Your turn! Input any number between 0-8')
        try:
            slot = int(move)
        except ValueError:
            raise

        if self.board[slot] == '  ':
            self.board[slot] = letter
        else:
            print('ERROR!!No available move in the specific SLOT!')
            exit()
        self.print_board()
        print('\n\n')
        if self.winner(slot, letter):
            print('YOU ARE THE WINNER!Congratulations!!!!')
            exit()
        if self.tie():
            print('It\'s a Tie!')
            exit()

    def comp_move(self, cletter):
        available_ind = list()
        for i in range(9):
            if self.board[i] == '  ':
                available_ind.append(i)
        move_now = random.choice(available_ind)
        self.board[move_now] = cletter
        self.print_board()
        print('\n\n')
        if self.winner(move_now, cletter):
            print('COMPUTER WON! YOU LOST! HAAHAHAHAHA!')
            exit()
        if self.tie():
            print('It\'s a Tie!')
            exit()

    def tie(self):
        if '  ' not in self.board:
            return True

    def winner(self, slot, letter):
        row_ind = math.floor(slot / 3)
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([s == letter for s in row]):
            return True
        col_ind = slot % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([s == letter for s in column]):
            return True
        if slot % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False


ttt = Game()
ttt.print_board_nums()
letter = input('X or O ?')

if letter == 'O':
    cletter = 'X' if letter == 'O' else 'O'
    while True:
        print('Computer\'s turn')
        time.sleep(0.3)
        ttt.comp_move(cletter)
        ttt.get_move(letter)
else:
    cletter = 'X' if letter == 'O' else 'O'
    while True:
        ttt.get_move(letter)
        print('Computer\'s turn')
        time.sleep(0.3)
        ttt.comp_move(cletter)
