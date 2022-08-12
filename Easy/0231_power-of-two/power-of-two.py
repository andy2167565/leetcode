class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
#======== <Solution 1> ========#
        return n > 0 and n & (n - 1) == 0

#======== <Solution 2> ========#
        return n > 0 and sum(list(map(int, bin(n)[2:]))) == 1

#======== <Solution 3> ========#
        return n > 0 and 2 ** 30 % n == 0
