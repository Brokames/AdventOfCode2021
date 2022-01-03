import functools as funct

def main():
    # Take in Data
    with open("C:\\Users\\Ja\\PycharmProjects\\AdventOfCode\\Day4Data.txt", 'r') as fd:
        lines = fd.readlines()
    # Make boards
    boards = []
    for i in range(100):
        boards += [BingoBoard(lines[i * 6: 5 + i * 6])]
    
    # Read in numbers and check
    bingo_vals = [int(x) for x in lines[-1].split(",")]
    valid_boards = [1] * 100
    for val in bingo_vals:
        for i, board in enumerate(boards):
            if valid_boards[i] == 1 and board.remove_num(val) and board.is_winner():
                if valid_boards.count(1) != 1:
                    valid_boards[i] = 0
                else:
                    print(board.give_sum() * val)
                    return



class BingoBoard:
    def __init__(self, board):
        self.board = []
        for i in range(5):
            str_list = board[i].rstrip('\n').split()
            self.board += [[int(x) for x in str_list]]

    def remove_num(self, num):
        for i in range(5):
            for j in range(5):
                if self.board[i][j] == num:
                    self.board[i][j] = -1
                    return 1
        return 0
    
    def is_winner(self):
        # Row
        for i in range(5):
            if all(element == -1 for element in self.board[i]):
                return 1
        # Column
        for i in range(5):
            test = [0] * 5
            for j in range(5):
                test[j] = self.board[j][i]
            if all(element == -1 for element in test):
                return 1
        return 0

    
    def give_sum(self):
        sum = 0
        for i in range(5):
            for j in range(5):
                if self.board[i][j] != -1:
                    sum += self.board[i][j]
        return sum


    def print_board(self):
        for i in range(5):
            for j in range(5):
                print(self.board[i][j], end=" ")
            print()
    


if __name__ == "__main__":
    main()
