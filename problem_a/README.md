# Problem 25
This script solve problem 25 on projecteuler.com
https://projecteuler.net/problem=25

## Problem:
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

## Solution A:
We can use the digits given to set up a dictionary, and then use the python cache for subsequent calls as we calculate up to the first 1000 digit
## Solution B:
It is possible there is a more mathimatical way to figure out the solution. I could probably graph the points given to see the curve, then figure out where something with 1000 intersects with the curve

The code is for Solution A
"""
