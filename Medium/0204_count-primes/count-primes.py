class Solution:
    def countPrimes(self, n: int) -> int:
#======== <Solution 1> ========#
        if n < 3: return 0
        isPrime = [False] * 2 + [True] * (n-2)
        for p in range(2, n):
            if isPrime[p]:
                num = p*p
                if num > n: break
                while num < n:
                    isPrime[num] = False
                    num += p
        return sum(isPrime)

#======== <Solution 2> ========#
        if n < 3: return 0
        isPrime = [False] * 2 + [True] * (n-2)
        for p in range(2, math.isqrt(n)+1):  # p*p < n -> p < sqrt(n)
            if isPrime[p]:
                for num in range(p*p, n, p):  # Mark in increments of p from p*p to n
                    isPrime[num] = False
        return sum(isPrime)

#======== <Solution 3> ========#
        if n < 3: return 0
        isPrime = [0] * 2 + [1] * (n-2)
        p = 2
        while p*p < n:
            if isPrime[p] == 1:
                # (1 + (n - 1 - p*p) // p) is equal to the number of multiples of p from p*p to n
                # Refer to Arithmetic Sequence: https://en.wikipedia.org/wiki/Arithmetic_progression
                isPrime[p*p: n: p] = [0] * (1 + (n - 1 - p*p) // p)
            # Add 1 to p if it is the first iteration so that p will be 3 in the next iteration
            # After that add 2 to p in each iteration to avoid checking even numbers again
            p += 1 if p == 2 else 2
        return sum(isPrime)
