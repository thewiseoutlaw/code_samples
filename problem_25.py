#!usr/bin/env python3
from datetime import datetime
from functools import lru_cache
import argparse
"""
This script solve problem 25 on projecteuler.com
https://projecteuler.net/problem=25

Problem:
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

Solution A:
    We can use the digits given to set up a dictionary, and then use the python cache for subsequent calls as we calculate up to the first 1000 digit
Solution B:
    It is possible there is a more mathimatical way to figure out the solution. I could probably graph the points given to see the curve, then figure out where something with 1000 intersects with the curve

Will attempt Solution A below
"""
FIB_DICT = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    7: 13,
    8: 21,
    9: 34,
    10: 55,
    11: 89,
    12: 144
}

@lru_cache(maxsize=3)
def fib(seq_num: int) -> int:
    global FIB_DICT
    if seq_num in FIB_DICT:
        return FIB_DICT[seq_num]
    else:
        return fib(seq_num-1) + fib(seq_num-2)

# for running as a script
if __name__ == "__main__":
    start = datetime.now()
    parser = argparse.ArgumentParser(description=
            "Calulates the first fibonacci index that hits a passed in number of digits")
    parser.add_argument('digits',
            type=int,
            help='the number of digits you wish to find a fib index for',
            default=1000
    )
    args = parser.parse_args()
    # we will keep the while loop going until we fine the input digit
    # start at 13 since it is not in the list
    test_fib = 13
    while True:
        result = fib(test_fib)
        if len(str(result)) >= args.digits:
            print("Index of fib", test_fib)
            print("The first number", result)
            break
        else:
            test_fib += 1
    print("Run in", datetime.now() - start)
