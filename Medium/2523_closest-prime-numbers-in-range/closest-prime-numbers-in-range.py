class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
#======== <Solution 1> ========#
        import collections
        isPrime = [False] * 2 + [True] * (right - 1)  # Initially mark all numbers as prime except for 0 and 1
        for i in range(2, int(right ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, right + 1, i):
                    isPrime[j] = False  # Mark all multiples as non-prime except for the first number
        if sum(isPrime[left: right + 1]) < 2: return [-1, -1]  # No prime or only 1 prime exists in the range
        dq, gap, ans = collections.deque(), float('inf'), []
        for i in range(left, right + 1):
            if isPrime[i]:
                dq.append(i)
                if len(dq) == 2:  # Compute gap when a pair of primes is collected
                    if dq[1] - dq[0] < gap:
                        gap, ans = dq[1] - dq[0], [dq[0], dq[1]]
                    dq.popleft()  # Drop previous prime for next pair
        return ans

#======== <Solution 2> ========#
        isPrime = [False] * 2 + [True] * (right - 1)
        for i in range(2, int(right ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i, right + 1, i):
                    isPrime[j] = False
        primes = [i for i in range(left, right + 1) if isPrime[i]]
        if len(primes) < 2: return [-1, -1]
        gap, ans = float('inf'), []
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < gap:
                gap, ans = primes[i + 1] - primes[i], [primes[i], primes[i + 1]]
        return ans
