class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
# Reference: https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/solutions/2230147/python-topo-dp-solution-and-dfs-solution/
#======== <Solution 1> ========#
        m, n, mod = len(grid), len(grid[0]), 10**9 + 7
        dp = [[1] * n for _ in range(m)]  # dp[i][j]: The number of paths ending at grid[i][j]
        for _, i, j in sorted((grid[i][j], i, j) for i in range(m) for j in range(n)):
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < grid[i][j]:
                    dp[i][j] += dp[ni][nj] % mod
        return sum(map(sum, dp)) % mod

#======== <Solution 2> ========#
        import functools
        m, n, mod = len(grid), len(grid[0]), 10**9 + 7

        @functools.cache
        def dfs(i, j):
            count = 1
            for di, dj in (0, 1), (0, -1), (1, 0), (-1, 0):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] < grid[i][j]:
                    count += dfs(ni, nj) % mod
            return count

        return sum(dfs(i, j) for i in range(m) for j in range(n)) % mod
