class Solution:
    def countDigits(self, num: int) -> int:
#======== <Solution 1> ========#
        ans, n = 0, num
        while n:
            n, val = divmod(n, 10)
            if not num % val:
                ans += 1
        return ans

#======== <Solution 2> ========#
        return sum(not num % int(val) for val in str(num))
