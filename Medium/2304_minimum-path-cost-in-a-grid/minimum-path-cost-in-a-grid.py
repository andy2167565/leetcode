class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import functools
        m, n = len(grid), len(grid[0])
        @functools.cache
        def dfs(i, j):
            return grid[i][j] + (min(dfs(i + 1, k) + moveCost[grid[i][j]][k] for k in range(n)) if i < m - 1 else 0)
        return min(dfs(0, j) for j in range(n))

#======== <Solution 2> ========#
        import functools
        m, n = len(grid), len(grid[0])
        @functools.cache
        def dfs(i, j):
            return grid[i][j] + (min(dfs(i - 1, k) + moveCost[grid[i - 1][k]][j] for k in range(n)) if i else 0)
        return min(dfs(m - 1, j) for j in range(n))

#======== <Solution 3> ========#
        import itertools
        costs = grid[0]
        for curr_row, next_row in itertools.pairwise(grid):
            costs = [min(cost + moveCost[curr_val][k] for cost, curr_val in zip(costs, curr_row)) + next_val for k, next_val in enumerate(next_row)]
        return min(costs)
