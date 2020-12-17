You should include with your solution:
• A sample of the output
• Why you chose the problems you did
• A description of the process you followed in solving the problem
• What reference sources you used, if any
• How much time you spent on the exercise

# Problem 205
Attempts to solve https://projecteuler.net/problem=205
```quote
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg
```
## Why I chose this problem
This seemed interesting since games theory and probability relates with statistics, machine learning, artificial intelligence and computer science topics where the algorithms can be re-used.

## Thoghts on how to solve
I thought of 2 ways I could possible solve. The first is what I ended up coding, which is a brute force approach.
- calculate all cartesian products for each player
- for each product, keep a dictionary of their sums and how many times we can create that sum
- For the person we are trying to beat, we need another dictionary, that sums all the ways we can win
    - So if in a standard game of dice where each player has one 6-sided dice, if I roll a 2, I can win in only 1 way - if my opponent rolls a 1
    - If i roll a 3 i can win in 2 ways, if my opponent rolls a 1 or 2
    - Increasing to both of us having 2 dice, if I roll a 4, I can win if my opponent rolls a 2 or 3
    - 2 can come up only one way, rolling two 1's
    - 3 can come up two ways, rolling a 1 and 2 and a 2 and 1.
    - so the total ways i can win when rolling a 4 with two dice, is 3.
- We can then loop through all possible numbers of Peter's rolls, and calculate chance of getting it and chance of Colin getting a smaller number

The other way I was thinking of was something mathimatical. I went through thinking about how probability works with dice and did some research on it.
Ultimately, it seems easier to use the above method since I can just program my way out of it. But below I went through my thoughts on probabilies.
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
    - == 1/4 chance of wining, makes since
- 2 pyramidal and 1 cubic? the range of values are 2 -> 8
    - 2 = 1/16 * 1/6
    - 3 = 2/16 * 2/6
    - 4 = 3/16 * 3/6
    - 5 = 4/16 * 4/6
    - 6 = 3/16 * 5/6
    - 7 = 2/16 * 6/6
    - 8 = 1/16 * 6/6
    - == 3/4
-  Can we figure out the pattern of how often each appears to just calculate what we need?
    - Peter 9*1 = 9, 9*4 = 36. 9 -> 36, total possibilities 4 ** 9
    - Colin 6*1 = 6, 6*6 = 36. 6 -> 36, total possibilities 6 ** 6
## References
- how to round decimal output
https://stackoverflow.com/questions/8568233/how-to-print-float-to-n-decimal-places-including-trailing-0s
- For looking up how probabilities work with dice
https://math.stackexchange.com/questions/460115/weighted-probability-problem
https://math.stackexchange.com/questions/866778/probability-of-winning-a-dice-game
- The fractions library, which I removed later, but used for testing to get out the probaility as a fraction
https://docs.python.org/3/library/fractions.html

## Time Spent on Problem
It took about an hour to figure out the probabilities
After that, I took another 45 minutes to code the solution and clean it up
1 hour and 45 minutes
## Output
 Chance for Peter to win: 0.5731441
 Time to run: 0:00:00.289298
