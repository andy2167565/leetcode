class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        preSumRow = [[0] * (n + 1) for _ in range(m)]  # Add one more column
        preSumCol = [[0] * (m + 1) for _ in range(n)]  # Add one more row
        for row in range(m):
            for col in range(n):
                preSumRow[row][col + 1] = preSumRow[row][col] + grid[row][col]
                preSumCol[col][row + 1] = preSumCol[col][row] + grid[row][col]

        def isMagicSquare(k):
            for row in range(m - k + 1):
                for col in range(n - k + 1):
                    diag = antiDiag = 0
                    for d in range(k):
                        diag += grid[row + d][col + d]
                        antiDiag += grid[row + d][col + k - 1 - d]
                    match = diag == antiDiag  # Check both diagonal sums
                    nrow, ncol = row, col
                    while nrow < row + k and match:  # Check every row sum
                        match = diag == preSumRow[nrow][col + k] - preSumRow[nrow][col]
                        nrow += 1
                    while ncol < col + k and match:  # Check every column sum
                        match = diag == preSumCol[ncol][row + k] - preSumCol[ncol][row]
                        ncol += 1
                    if match:  # All the sums are equal
                        return True
            return False

        for k in range(min(m, n), 1, -1):
            if isMagicSquare(k):  # The first valid k is the maximum result
                return k
        return 1
