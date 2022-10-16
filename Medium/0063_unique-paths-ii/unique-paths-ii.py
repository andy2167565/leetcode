class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#======== <Solution 1> ========#
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * (n - 1)  # Only record path at row level
        for i in range(m):  # Each row inherits dp from previous row, which indicates paths from upper grid
            for j in range(n):
                if obstacleGrid[i][j]:  # Reset paths when hitting the obstacle
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1] if j else 0  # Add paths from left grid
        return dp[-1]

#======== <Solution 2> ========#
        for i, row in enumerate(obstacleGrid):
            for j, val in enumerate(row):
                if obstacleGrid[i][j] or i == j == 0:
                    obstacleGrid[i][j] = 1 - val
                else:
                    obstacleGrid[i][j] += (obstacleGrid[i - 1][j] if i else 0) + (obstacleGrid[i][j - 1] if j else 0)
        return obstacleGrid[-1][-1]

# Reference: https://leetcode.com/problems/unique-paths-ii/discuss/2055409/Beginner-Friendly-%22Recursion-to-DP%22-Intuition-Explained-Python
#======== <Solution 3> ========#
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        @cache
        def dfs(i, j):
            if i == m or j == n or obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            return dfs(i + 1, j) + dfs(i, j + 1)
        return dfs(0, 0)

#======== <Solution 4> ========#
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == m or j == n or obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return dp[i][j]
        return dfs(0, 0)
