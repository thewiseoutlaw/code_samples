# Problem 205
Attempts to solve https://projecteuler.net/problem=205
## Problem:
    Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
    Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

    Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

    What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg

## Solution A -Brute Force (What is coded):
    - calculate all cartesian products for each player
    - for each permutation, keep a dictionary of their sums and how many times we can create that sum
    - For the person we are trying to beat, we need another dictionary, that sums all the ways we can win ( we being Peter)
    - We can then loop through all possible numbers of Peter's rolls, and calculate chance of getting it and chance of Colin getting a smaller number

## Solution B - Math:
    - So starting at 1 cubic dice each, let's figure out the probability of Pete wining then
        - 1 = 0/6, best is tie
        - 2 = 1/6, if Colin rolls 1
        - 3 = 2/6
        - 4 = 3/6
        - 5 = 4/6
        - 6 = 5/6
    - What about pyramidal dice? well it is the same but stops at 4, Let's use the proper weighted one
        - 1 = 1/4 * 0/6
        - 2 = 1/4 * 1/6
        - 3 = 1/4 * 2/6
        - 4 = 1/4 * 3/6
        == 1/4 chance of wining, makes since
    - 2 pyramidal and 1 cubic? the range of values are 2 -> 8
        - 2 = 1/16 * 1/6
        - 3 = 2/16 * 2/6
        - 4 = 3/16 * 3/6
        - 5 = 4/16 * 4/6
        - 6 = 3/16 * 5/6
        - 7 = 2/16 * 6/6
        - 8 = 1/16 * 6/6
        == 3/4
    - from here we need to calculate the range of numbers for each
        - Peter 9*1 = 9, 9*4 = 36. 9 -> 36, total possibilities 4 ** 9
        - Colin 6*1 = 6, 6*6 = 36. 6 -> 36, total possibilities 6 ** 6
