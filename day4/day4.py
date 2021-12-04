#!/usr/bin/env python


def read_data(path):
    with open(path) as f:
        data = f.read().strip().split("\n")
    numbers = list(map(int, data.pop(0).split(",")))
    data = data[1:]
    boards, board = [], []
    for line in data:
        if line == "":
            boards.append(board)
            board = []
        else:
            board.append(list(map(int, line.split())))
    return numbers, boards


class Board:
    def __init__(self, numbers):
        self.numbers = numbers
        self.marked = []
        self.n = len(numbers)  # assume square board
        self.is_winner_ = False

    def mark(self, number):
        for i in range(self.n):
            for j in range(self.n):
                if self.numbers[i][j] == number:
                    self.marked.append((i, j))
                    return

    def score(self):
        s = 0
        for i in range(self.n):
            for j in range(self.n):
                if (i, j) in self.marked:
                    continue
                else:
                    s += self.numbers[i][j]
        return s

    @property
    def is_winner(self):
        if self.is_winner_:
            return True
        else:
            self._check_win()
            return self.is_winner_

    def _check_win(self):
        for i in range(self.n):
            if len([x for x in self.marked if x[0] == i]) == self.n:
                self.is_winner_ = True
            if len([x for x in self.marked if x[1] == i]) == self.n:
                self.is_winner_ = True


def part1(numbers, boards):
    boards = [Board(board) for board in boards]
    for number in numbers:
        for board in boards:
            board.mark(number)
            if board.is_winner:
                return board.score() * number


def part2(numbers, boards):
    boards = [Board(board) for board in boards]
    for number in numbers:
        for board in boards:
            if board.is_winner:
                continue
            board.mark(number)
            if board.is_winner:
                last_winning_score = board.score()
                last_winning_number = number
    return last_winning_score * last_winning_number


def main():
    numbers, boards = read_data("input.txt")
    assert part1(numbers, boards) == 6592
    assert part2(numbers, boards) == 31755
    print("All tests passed.")


if __name__ == "__main__":
    main()
