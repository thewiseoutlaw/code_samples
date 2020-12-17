#!/usr/bin/env python3
"""
This script provides a solution to https://projecteuler.net/problem=96

It reads in the txt file of sudoku puzzles from the site, and sends it to an api to solve each one.
The output is the sum of the top left 3-digit number of each solved puzzle.

ex. of input text
Grid 01
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300

"""
import argparse
from datetime import datetime
from sudoku import Sudoku

def parse_sudoku(input_file) -> list:
    """ parse file to list of grids """
    all_boards = list()
    with open(input_file) as f:
        for line in f:
            if line.startswith('G'):
                board = list()
                continue
            # map the string chars to ints
            row = list()
            for c in line.strip():
                row.append(int(c))
            board.append(row)
            if len(board) == 9:
                # have all 9 rows
                all_boards.append(board)
    return all_boards

def solve_single_board(board):
    """ Solves a single standard size sudoku board """
    puzzle = Sudoku(3, 3, board=board)
    return puzzle.solve()

def solve_boards(boards):
    """ Takes in a list of boards to solve and prints the solution out
        Also returns the projecteuler solution
    """
    sum_of_top = 0
    for board in boards:
        solution = solve_single_board(board)
        solution.show_full()
        # Convert the top left chars to a string and than add to sum
        top_3_nums = int(str(solution.board[0][0]) + str(solution.board[0][1]) + str(solution.board[0][2]))
        sum_of_top +=top_3_nums
    return sum_of_top


if __name__ == '__main__':
    start = datetime.now()
    parser = argparse.ArgumentParser(description=
            "Solves a list of sudoku puzzles")
    parser.add_argument('puzzle_file',
            type=str,
            help='The file with the list of puzzles, Grids seperated by the name "Grid x" ',
    )
    args = parser.parse_args()
    boards = parse_sudoku(args.puzzle_file)
    sum_of_top = solve_boards(boards)
    print("The sum of the all puzzles top 3 digits:", sum_of_top)
    print("Run in", datetime.now() - start)
