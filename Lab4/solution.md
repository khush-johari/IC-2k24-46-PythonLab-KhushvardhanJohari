Q1-What do you think makes one piece of code faster than another that produces the same output? Write your guess in one or two lines, before doing anything else here.

Ans-One piece of code is faster because it takes fewer steps, uses less memory, or accesses data more efficiently.


Q2-Name any Python function or technique you already know that helps avoid repeating work. If none, write "none yet" and come back to this at the end.

Ans-


Section B: Problem 1, Sum of All Primes Below N

Step 1: Naive Version

Write a program that computes the sum of all prime numbers strictly below N, checking every number from 2 up to N minus 1, and for each one, testing all possible divisors to decide if it is prime.

Naive version, N = 50,000, Time taken:  approx 5s
Naive version, N = 2,000,000, Time taken:  indefinite

3. What did you observe? Did the time grow the way you expected when N grew by about 40 times?
Step 2: Hint 1
When checking whether a number x is prime, do you really need to test every divisor up to x minus 1? Write the smallest upper bound you actually need to check up to, and why that is still enough to correctly determine primality.
Rewrite your program using this smaller bound. Test with N = 2,000,000.
Smaller bound version, N = 2,000,000, Time taken:  6sec (approx)

the naive time grows quadratically. When $N$ grows 40x, the time roughly grows by $40^2$ (1600x) because you are doing more checks for a larger amount of numbers.


4. How much faster was this compared to Step 1? Was it enough, or still slow?
Step 3: Hint 2
Your current approach solves "is this number prime" separately, from scratch, for every number. What if you solved "which numbers up to N are prime" all in one pass? This technique is called the Sieve of Eratosthenes.
Write, in your own words, the core idea of how the sieve works, before writing any code.


Implement the sieve. Test with N = 2,000,000.
Sieve version, N = 2,000,000, Time taken:  0.17427sec 

The upper bound needed is \|-x(under root). It is much faster, but for $N = 2,000,000$, checking every number individually is still too slow.

5. Compare all three times for N = 2,000,000 side by side.
Naive:              indefinite 
Smaller bound:       6.71706s
Sieve:                0.17427s

6. Which single change gave the biggest jump in speed? Explain why.

The Sieve of Eratosthenes gives the biggest jump. It completely eliminates division operations and avoids redundant checks by marking multiples in a single sweep.
