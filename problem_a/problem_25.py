#!usr/bin/env python3
from datetime import datetime
from functools import lru_cache
import argparse
"""
This script solve problem 25 on projecteuler.com
https://projecteuler.net/problem=25
"""
# Since this dictionary was provided, I might was well use it for speed
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
# Using the lru_cache allows us to save on heap space since we just need the last previous 2 results
@lru_cache(maxsize=3)
def fib(seq_num: int) -> int:
    global FIB_DICT
    if seq_num in FIB_DICT:
        return FIB_DICT[seq_num]
    else:
        return fib(seq_num - 1) + fib(seq_num - 2)

def index_of_fib(digits):
    test_fib = 1
    while True:
        result = fib(test_fib)
        if len(str(result)) >= args.digits:
            break
        else:
            test_fib += 1
    return test_fib

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
    print("Index of fib: ", index_of_fib(args.digits))
    # we will keep the while loop going until we fine the input digit
    print("Run in", datetime.now() - start)
