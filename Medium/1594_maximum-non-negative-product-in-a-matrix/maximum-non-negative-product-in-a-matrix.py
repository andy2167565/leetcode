class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        import functools
        @functools.cache
        def dfs(i, j):  # Return maximum & minimum products ending at (i, j)
            if not i and not j:
                return grid[0][0], grid[0][0]
            if i < 0 or j < 0:
                return float('-inf'), float('inf')
            if not grid[i][j]:
                return 0, 0
            max_prod_top, min_prod_top = dfs(i - 1, j)
            max_prod_left, min_prod_left = dfs(i, j - 1)
            max_prod, min_prod = max(max_prod_top, max_prod_left) * grid[i][j], min(min_prod_top, min_prod_left) * grid[i][j]
            return (max_prod, min_prod) if grid[i][j] > 0 else (min_prod, max_prod)
        
        max_prod, _ = dfs(len(grid) - 1, len(grid[0]) - 1)
        return -1 if max_prod < 0 else max_prod % (10**9 + 7)
