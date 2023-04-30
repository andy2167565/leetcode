class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n, directions = len(grid), len(grid[0]), [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(r, c, fish=0):
            fish += grid[r][c]
            grid[r][c] = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc]:
                    fish += dfs(nr, nc)
            return fish
        ans = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    ans = max(ans, dfs(r, c))
        return ans
