class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
#======== <Solution 1> ========#
        m, n = len(grid), len(grid[0])
        dp = [grid[0][0]] + [float('inf')] * (n - 1)
        for i in range(m):
            for j in range(n):
                if not i == j == 0:
                    dp[j] = grid[i][j] + min(dp[j - 1], dp[j])
        return dp[-1]

#======== <Solution 2> ========#
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not i == j == 0:
                    grid[i][j] += min(grid[i - 1][j] if i else float('inf'), grid[i][j - 1] if j else float('inf'))
        return grid[-1][-1]

#======== <Solution 3> ========#
        m, n = len(grid), len(grid[0])
        @cache
        def dfs(i, j):
            if i == m - 1 and j == n - 1:  # Reach the bottom-right grid
                return grid[i][j]
            if i == m or j == n:  # Out of boundary
                return float('inf')
            return grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
        return dfs(0, 0)

#======== <Solution 4> ========#
        m, n = len(grid), len(grid[0])
        dp = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if i == m or j == n:
                return float('inf')
            if dp[i][j] != -1:  # Return the value directly if dp[i][j] is updated
                return dp[i][j]
            dp[i][j] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
            return dp[i][j]
        return dfs(0, 0)
