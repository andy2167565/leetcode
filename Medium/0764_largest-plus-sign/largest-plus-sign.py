class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/largest-plus-sign/solutions/113314/java-c-python-o-n-2-solution-using-only-one-grid-matrix/
        grid = [[n] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        for i in range(n):
            l = r = u = d = 0
            for j, k in zip(range(n), reversed(range(n))):
                l = l + 1 if grid[i][j] else 0
                grid[i][j] = min(grid[i][j], l)
                r = r + 1 if grid[i][k] else 0
                grid[i][k] = min(grid[i][k], r)
                u = u + 1 if grid[j][i] else 0
                grid[j][i] = min(grid[j][i], u)
                d = d + 1 if grid[k][i] else 0
                grid[k][i] = min(grid[k][i], d)
        return max(map(max, grid))
