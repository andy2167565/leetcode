class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        def lcs(s1, s2):  # Longest Common Sequence
            m, n = len(s1), len(s2)
            dp = [['' for _ in range(n + 1)] for _ in range(m + 1)]
            for i in range(m):
                for j in range(n):
                    if s1[i] == s2[j]:
                        dp[i + 1][j + 1] = dp[i][j] + s1[i]
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            return dp[-1][-1]

        res, i, j = '', 0, 0
        for c in lcs(str1, str2):
            while str1[i] != c:
                res += str1[i]
                i += 1
            while str2[j] != c:
                res += str2[j]
                j += 1
            res += c
            i, j = i + 1, j + 1
        return res + str1[i:] + str2[j:]
