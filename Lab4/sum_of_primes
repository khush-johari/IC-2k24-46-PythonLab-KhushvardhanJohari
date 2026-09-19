import time
import math

def solve_primes(N):
    # Step 1: Naive 
    # (Sum is calculated alongside search via `ans_naive += i`)
    start = time.time()
    ans_naive = 0
    for i in range(2, N):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime: 
            ans_naive += i
    t_naive = time.time() - start

    # Step 2: Smaller Bound (Square Root)
    # (Sum is calculated alongside search via `ans_bound += i`)
    start = time.time()
    ans_bound = 0
    for i in range(2, N):
        is_prime = True
        for j in range(2, int(math.isqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime: 
            ans_bound += i
    t_bound = time.time() - start

    # Step 3: Sieve of Eratosthenes
    # (Updated to calculate the sum alongside the search)
    start = time.time()
    is_prime = [True] * N
    is_prime[0] = is_prime[1] = False
    
    ans_sieve = 0
    for i in range(2, N):
        if is_prime[i]:
            ans_sieve += i  # Add to sum immediately when a prime is found
            
            # Cross out multiples (only necessary if i*i is within bounds)
            if i * i < N:
                for j in range(i * i, N, i):
                    is_prime[j] = False
    t_sieve = time.time() - start

    # Print results
    print(f"Times -> Naive: {t_naive:.5f}s | Bound: {t_bound:.5f}s | Sieve: {t_sieve:.5f}s")
    print(f"Sums  -> Naive: {ans_naive} | Bound: {ans_bound} | Sieve: {ans_sieve}/n")

solve_primes(50000)
#solve_primes(2000000) Would crash on my machine due to memory constraints, but should work fine on a more powerful machine

