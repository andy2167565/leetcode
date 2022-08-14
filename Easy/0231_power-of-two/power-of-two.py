class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
#======== <Solution 1> ========#
        return n > 0 and 2**30 % n == 0

#======== <Solution 2> ========#
        import math
        return n > 0 and (math.log10(n) / math.log10(2)) % 1 == 0

#======== <Solution 3> ========#
        if n < 1: return False
        while n % 2 == 0:
            n //= 2
        return n == 1

#======== <Solution 4> ========#
        if n < 1: return False
        if n == 1: return True
        return n % 2 == 0 and self.isPowerOfTwo(n // 2)

#======== <Solution 5> ========#
        return n > 0 and n & (n - 1) == 0

#======== <Solution 6> ========#
        return n > 0 and sum(list(map(int, bin(n)[2:]))) == 1
