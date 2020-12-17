# Problem 25
This script solve problem 25 on projecteuler.com
https://projecteuler.net/problem=25

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
## Why I chose this problem
Fibonacci is a familiar concept from my college days. This looked like a good problem to warm-up on. It also provided a way to use python built in lru_cache
to optimize both time and memory used in one go
## Thoughts on how I solved the problem
First thing i thought of - We can use the digits given to set up a dictionary, and then use the python cache for subsequent calls as we calculate up to the first 1000 digit number. This should be fairly effient and not take too much time to set up. Plus we are given the first 12 numbers in the Fibonacci sequence.

While I ended up coding the above, I thought their could possibly be a faster way. I could probably graph the points given to see the curve, then figure out where something with 1000 digits appears on the line. This might be a good approximation, but probably wouldn't get me the exact index. 
"""

## References
for timing of test
https://stackoverflow.com/questions/6786990/find-out-time-it-took-for-a-python-script-to-complete-execution

looked up argparse documentation
https://docs.python.org/3/library/argparse.html
## Time spent solving
Took about 15 minutes to code a first solution and another 10 minutes to clean it up
Total time: 25 minutes
## Output
```bash
> python3 problem_25.py -h
usage: problem_25.py [-h] digits

Calulates the first fibonacci index that hits a passed in number of digits

positional arguments:
digits      the number of digits you wish to find a fib index for

optional arguments:
-h, --help  show this help message and exit
```
```bash
python3 problem_25.py 1000
Index of fib:  4782
Run in 0:00:00.029102
```
