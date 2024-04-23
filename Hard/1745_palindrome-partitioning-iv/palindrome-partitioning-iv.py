class Solution:
    def checkPartitioning(self, s: str) -> bool:
        # Reference: https://leetcode.com/problems/palindrome-partitioning-iv/solutions/1043180/java-python-bottom-up-dp-clean-concise-o-n-2/
        n = len(s)
        dp = [[False] * n for _ in range(n)]  # dp[i][j]: Substring s[i: j + 1] is a palindrome or not
        for i in range(n - 1, -1, -1):
            for j in range(n):
                if i >= j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
        return any(dp[0][i - 1] and dp[i][j - 1] and dp[j][n - 1] for i in range(1, n) for j in range(i + 1, n))
