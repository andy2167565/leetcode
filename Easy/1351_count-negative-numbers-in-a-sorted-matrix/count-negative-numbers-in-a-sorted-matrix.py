class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, ans = len(grid[0]), 0
        for row in grid:
            for i, num in enumerate(row):
                if num < 0:
                    ans += n - i
                    break
        return ans
