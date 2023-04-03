class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0  # Sink non-enclave land cell
            for di, dj in directions:
                x, y = i + di, j + dj
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)
        m, n, directions = len(grid), len(grid[0]), [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i in (0, m - 1) or j in (0, n - 1)):  # Reset the land cells on the boundary and all adjacent land cells
                    dfs(i, j)
        return sum(map(sum, grid))
