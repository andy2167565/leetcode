class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        # Reference: https://leetcode.com/problems/maximize-number-of-nice-divisors/discuss/1130495/Python-O(log-n)-math-solution-explained
        if primeFactors < 4: return primeFactors
        mod = 10**9 + 7
        q, r = divmod(primeFactors, 3)
        if r == 1: return 4 * pow(3, q - 1, mod) % mod
        return (1 + (r > 0)) * pow(3, q, mod) % mod
