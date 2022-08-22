class Solution:
    def minOperations(self, n: int) -> int:
#======== <Solution 1> ========#
        return sum(n - (2 * i + 1) for i in range(n // 2))

#======== <Solution 2> ========#
        return n * n // 4
