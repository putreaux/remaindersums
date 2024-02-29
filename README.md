# Sums of remainders #

This program calculates sums of all remainders of integers divided by integers smaller than them. This is calculated up to N, such that for all integers the sum is plotted with prime numbers being marked with a red dot and composite numbers with a blue dot.

The summation for each integer from 2 to N works as:

$X_N = \sum\limits^N_{i=2} \frac{N}{i} - \lfloor \frac{N}{i} \rfloor$.

The sums are relatively close to each other in terms of the x index, so the slope of the sums can be subtracted from the sums to create a new x axis representing average sum per integer. It is calculated as

$\frac{1}{a} \sum\limits^N_{i=2} X_i$,

where a is a total number of additions to all sums combined, for each i. The resulting slope is therefore the average remainder. 


For example, summing the remainders for number 5 goes like this: 

$X_5 = (\frac{5}{2} - 2) + (\frac{5}{3} - 1) + (\frac{5}{4} - 1) \\
= ~1.41666...$

## Running the code ##


