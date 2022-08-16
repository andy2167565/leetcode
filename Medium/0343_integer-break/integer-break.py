class Solution:
    def integerBreak(self, n: int) -> int:
#======== <Solution 1> ========#
        if n < 4: return n - 1
        q, r = divmod(n, 3)
        if r == 1: return 4 * 3**(q - 1)
        return (1 + (r > 0)) * 3**q

#======== <Solution 2> ========#
        dp = [None, None, 1, 2, 4, 6, 9]
        for i in range(7, n + 1):
            dp.append(dp[i - 3] * 3)
        return dp[n]
