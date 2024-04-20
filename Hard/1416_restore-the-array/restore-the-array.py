class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [1] * (len(s) + 1)  # dp[i]: The number of possible ways for s[:i]
        for i in range(len(s)):
            count, curr = 0, ''
            for j in range(i, max(-1, i - len(str(k))), -1):
                curr = s[j] + curr
                if curr[0] != '0' and int(curr) <= k:  # Found a valid number
                    count += dp[j]
            if not count:
                return 0
            dp[i + 1] = count % (10**9 + 7)
        return dp[-1]
