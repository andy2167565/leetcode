class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
#======== <Solution 1> ========#
        m, n = len(grid), len(grid[0])
        diffRow, diffCol = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                offset = grid[i][j] * 2 - 1
                diffRow[i] += offset  # diffRow[i] = onesRow[i] - zerosRow[i]
                diffCol[j] += offset  # diffCol[j] = onesCol[j] - zerosCol[j]
        for i in range(m):
            for j in range(n):
                grid[i][j] = diffRow[i] + diffCol[j]
        return grid

#======== <Solution 2> ========#
        import itertools
        m, n = len(grid), len(grid[0])
        countDiff = lambda nums: 2 * sum(nums) - len(nums)
        diffRow = list(map(countDiff, grid))
        diffCol = list(map(countDiff, zip(*grid)))
        for i, j in itertools.product(range(m), range(n)):
            grid[i][j] = diffRow[i] + diffCol[j]
        return grid
