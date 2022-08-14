class Solution:
    def isPowerOfThree(self, n: int) -> bool:
#======== <Solution 1> ========#
        return n > 0 and 3**19 % n == 0

#======== <Solution 2> ========#
        import math
        return n > 0 and (math.log10(n) / math.log10(3)) % 1 == 0

#======== <Solution 3> ========#
        if n < 1: return False
        while n % 3 == 0:
            n //= 3
        return n == 1

#======== <Solution 4> ========#
        if n < 1: return False
        if n == 1: return True
        return n % 3 == 0 and self.isPowerOfThree(n // 3)
