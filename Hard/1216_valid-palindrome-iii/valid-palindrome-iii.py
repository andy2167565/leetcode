class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Reference: https://leetcode.com/problems/valid-palindrome-iii/solutions/397634/python3-edit-distance/
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                if not i or not j:
                    dp[i][j] = i or j
                elif s[i - 1] == s[n - j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])
        return dp[n][n] <= k * 2
