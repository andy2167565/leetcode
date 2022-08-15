class Solution:
    def myPow(self, x: float, n: int) -> float:
#======== <Solution 1> ========#
        ans, val = 1, abs(n)
        while val:
            if val % 2: ans *= x
            x *= x
            val //= 2
        return 1 / ans if n < 0 else ans

#======== <Solution 2> ========#
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, abs(n))
        return x * self.myPow(x, n - 1) if n % 2 else self.myPow(x * x, n // 2)

#======== <Solution 3> ========#
        return pow(x, n)
