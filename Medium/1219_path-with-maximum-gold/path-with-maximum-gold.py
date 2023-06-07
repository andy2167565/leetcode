class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(i, j, gold):
            if 0 <= i < m and 0 <= j < n and grid[i][j]:
                curr_gold, grid[i][j] = grid[i][j], 0
                gold = max(dfs(r, c, gold + curr_gold) for r, c in ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)))
                grid[i][j] = curr_gold  # Backtracking
            return gold
        return max(dfs(i, j, 0) for i in range(m) for j in range(n))
