#!/usr/bin/env python3
import collections
import itertools
from datetime import datetime
"""
This script 

See README.md for detailed explanation of logic
"""
class DiceCollection():
    def __init__(self, sides: int, count: int):
        self.sides = sides
        self.count = count
        #defaultdict(int) sets any key not in the dict to 0
        self.possiblities_count = collections.defaultdict(int)
        self.denominator = sides ** count
        # range is exclusive of end number
        cartesian_product = itertools.product(range(1, sides+1), repeat=self.count)
        for roll in cartesian_product:
            self.possiblities_count[sum(roll)] += 1

    def chance_to_win(self, opponent) -> float:
        """
        Returns the chance of this dice winning against an opponent
        """
        # sum up all possible ways to get that number OR less
        opponent_sums = collections.defaultdict(int)
        # lowest number we can get all 1's. Same as number of sides * 1
        start_range = 1 * opponent.count
        # highest number on a dice is the same as the number of sides of the dice ( 6 sided dice highest number is 6)
        # highest sum we can achieve than is that number * the count
        # add 1 since the end range is exclusive
        end_range = opponent.sides * opponent.count + 1
        for i in range(opponent.sides, end_range):
            opponent_sums[i] = opponent.possiblities_count[i] + opponent_sums[i-1]
        # Using above we can figure out for each number this dice rolls, how many way it can beat the opponent
        total_chances = 0
        for i in range(1, self.denominator+1):
            numerator = self.possiblities_count[i]
            # total_chances += Fraction(numerator/self.denominator) * Fraction(opponent_sums[i-1]/opponent.denominator)
            total_chances += numerator/self.denominator * opponent_sums[i-1]/opponent.denominator
        return total_chances

if __name__ == '__main__':
    start = datetime.now()
    peter = DiceCollection(4, 9)
    colin = DiceCollection(6, 6)
    print(f"{peter.chance_to_win(colin):.7}")
    # we will keep the while loop going until we fine the input digit
    delta = datetime.now() - start
    print('Time to run:', delta)
