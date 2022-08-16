class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#======== <Solution 1> ========#
        from math import factorial
        return factorial((m - 1) + (n - 1)) // (factorial(m - 1) * factorial(n - 1))

#======== <Solution 2> ========#
        from math import comb
        return comb((m - 1) + (n - 1), m - 1)
