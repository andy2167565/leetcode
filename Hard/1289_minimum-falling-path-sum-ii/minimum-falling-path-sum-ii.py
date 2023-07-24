class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        import heapq
        for i in range(1, len(grid)):
            prev = heapq.nsmallest(2, grid[i - 1])  # Find the 2 minimum values in the previous row
            for j in range(len(grid[0])):
                grid[i][j] += prev[1] if grid[i - 1][j] == prev[0] else prev[0]
        return min(grid[-1])
