class Solution:
    def isPowerOfFour(self, n: int) -> bool:
#======== <Solution 1> ========#
        import math
        return n > 0 and (math.log10(n) / math.log10(4)) % 1 == 0

#======== <Solution 2> ========#
        if n < 1: return False
        while n % 4 == 0:
            n //= 4
        return n == 1

#======== <Solution 3> ========#
        if n < 1: return False
        if n == 1: return True
        return n % 4 == 0 and self.isPowerOfFour(n // 4)

#======== <Solution 4> ========#
        # Reference: https://ithelp.ithome.com.tw/articles/10240132
        return n & (n - 1) == 0 and n & 0x55555555 != 0

#======== <Solution 5> ========#
        return n > 0 and n & (n - 1) == 0 and len(bin(n)) % 2 == 1

#======== <Solution 6> ========#
        return n & (n - 1) == 0 and (n % 3) & 1 == 1
