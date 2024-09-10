class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
#======== <Solution 1> ========#
        return n * (n % 2 + 1)

#======== <Solution 2> ========#
        return n << (n & 1)
