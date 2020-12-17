# Problem 96
## Why I chose this problem
I am familiar with sudoku puzzles and enjoy solving them, so I decided this would be a good problem to solve.

## Thoughts to getting to a solution
At first I thought of creating a solver myself
  - For each cell, calculate all possible values it can hold, (check the row, column, and the 3x3 square for all numbers)
  - We can keep track by putting a tuple of each cell in a dictionary, and set of the numbers that can fill it
  - find any key with only one value and set that as the value for that cell in the solution grid, and remove it from rows, cols and 3x3
    - i.e for row 3, col 6 and possible values 2,3,4 == dict((3,6): {2,3,4})
  - If you can't find any 1 value, then look for a unique value in a row, col or 3x3
  - if you can't do that, you have to try a value in a cell that only has a few left in a depth first search fashion. 

Then I thought this would be a case of not reinventing the wheel and either looking for an API, or some other library to solve sudoku's
Their are some APIs https://rapidapi.com/sosier/api/solve-sudoku/details, but they require an API key and I did not want to upload that with my code, since it would be insecure, but would have shown my ability to use the requests module in python to send json payloads and parse responses.

Instead I used a python library https://github.com/jeffsieu/py-sudoku, and Pipenv to install it. Then the problem became properly parsing text input to solve each board and gathering the numbers needed to output the solution

## References
Python library for solving sudoku - https://github.com/jeffsieu/py-sudoku
API for solving sudoku - https://rapidapi.com/sosier/api/solve-sudoku/details

## Time spent on problem
Around 20 minutes coding
Around 20 minutes looking for an API and reading the docs to see if it would be suitable. 

## Output:
```bash
> python problem_96.py -h
usage: problem_96.py [-h] puzzle_file

Solves a list of sudoku puzzles

positional arguments:
  puzzle_file  The file with the list of puzzles, Grids seperated by the name "Grid x"

optional arguments:
  -h, --help   show this help message and exit
```
```bash
> python3 problem_96.py p096_sudoku.txt

---------------------------
9x9 (3x3) SUDOKU PUZZLE
Difficulty: SOLVED
---------------------------
+-------+-------+-------+
| 3 5 1 | 2 8 6 | 4 9 7 |
| 4 9 2 | 1 5 7 | 6 3 8 |
| 7 8 6 | 9 3 4 | 5 1 2 |
+-------+-------+-------+
| 2 7 5 | 4 6 9 | 1 8 3 |
| 9 3 8 | 5 2 1 | 7 6 4 |
| 6 1 4 | 8 7 3 | 2 5 9 |
+-------+-------+-------+
| 8 2 9 | 6 4 5 | 3 7 1 |
| 1 6 3 | 7 9 2 | 8 4 5 |
| 5 4 7 | 3 1 8 | 9 2 6 |
+-------+-------+-------+
The sum of the all puzzles top 3 digits: 24702
Run in 0:00:00.506262
```
