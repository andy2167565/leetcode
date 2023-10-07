class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        def dropBall(col):
            for row in range(m):
                ncol = col + grid[row][col]
                if ncol < 0 or ncol >= n or grid[row][ncol] != grid[row][col]:
                    return -1
                col = ncol
            return col
        return map(dropBall, range(n))
