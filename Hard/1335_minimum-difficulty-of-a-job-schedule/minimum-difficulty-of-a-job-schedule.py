class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/solutions/924611/dfs-dp-progression-with-explanation-o-n-3d-o-nd/
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[float('inf')] * d for _ in range(n)]  # dp[i][j]: The minimum difficulty of the schedule including first (i + 1) jobs partitioned into (j + 1) days
        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], jobDifficulty[i])
        for i in range(1, n):
            for j in range(1, min(i + d, d)):
                maxd = 0
                for k in range(i - 1, -1, -1):
                    maxd = max(maxd, jobDifficulty[k + 1])
                    dp[i][j] = min(dp[i][j], dp[k][j - 1] + maxd)
        return dp[-1][-1]
