class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
# Reference (Explanation): https://leetcode.com/problems/count-ways-to-build-good-strings/discuss/2807238/Full-Explanation-oror-Easy-to-understand
#======== <Solution 1> ========#
        dp = [1] + [0] * high  # dp[i]: Number of strings with length i. dp[0] = 1 which indicates an empty string [""]
        mod = 10**9 + 7
        for i in range(high):
            if i + zero <= high:
                dp[i + zero] = (dp[i + zero] + dp[i]) % mod
            if i + one <= high:
                dp[i + one] = (dp[i + one] + dp[i]) % mod
        return sum(dp[low: high + 1]) % mod

#======== <Solution 2> ========#
        dp = [1] + [0] * high
        mod, ans = 10**9 + 7, 0
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % mod
            # If i - zero < 0 or i - one < 0, dp[i - zero] or dp[i - one] are always unprocessed dp values from the end of array, i.e., always equal to 0
            # e.g. low = 5, high = 5, zero = 5, one = 1
            # dp = [1, 0, 0, 0, 0, 0]
            # dp[1] = dp[-4] + dp[0] = 0 + 1 = 1
            # dp[2] = dp[-3] + dp[1] = 0 + 1 = 1
            # dp[3] = dp[-2] + dp[2] = 0 + 1 = 1
            # dp[4] = dp[-1] + dp[3] = 0 + 1 = 1
            # dp[5] = dp[0] + dp[4] = 1 + 1 = 2
            if low <= i <= high:
                ans = (ans + dp[i]) % mod
        return ans

#======== <Solution 3> ========#
        import collections
        dp = collections.Counter({0: 1})
        mod = 10**9 + 7
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % mod
        return sum(dp[i] for i in range(low, high + 1)) % mod

#======== <Solution 4> ========#
        mod = 10**9 + 7
        @cache
        def dfs(i):
            if not i: return 1
            if i < 0: return 0
            return (dfs(i - zero) + dfs(i - one)) % mod
        return sum(dfs(i) for i in range(low, high + 1)) % mod
