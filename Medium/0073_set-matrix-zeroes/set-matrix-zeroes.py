class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
# Reference 1: https://leetcode.com/problems/set-matrix-zeroes/solutions/657430/python-solution-w-approach-explanation-readable-with-space-progression-from-o-m-n-o-1/
# Reference 2: https://leetcode.com/problems/set-matrix-zeroes/solutions/1469077/python-from-o-m-n-space-to-o-1-space-with-picture-clean-concise/
#======== <Solution 1> ========#
        m, n = len(matrix), len(matrix[0])
        zeroRow, zeroCol = [False] * m, [False] * n  # Mark the rows and columns that contains zero
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    zeroRow[i] = zeroCol[j] = True  # Mark row i and column j
        for i in range(m):
            for j in range(n):
                if zeroRow[i] or zeroCol[j]:
                    matrix[i][j] = 0

#======== <Solution 2> ========#
        m, n = len(matrix), len(matrix[0])
        # Check if first row and first column contain zero
        zeroFirstRow = any(not matrix[0][j] for j in range(n))
        zeroFirstCol = any(not matrix[i][0] for i in range(m))
        # Iterate through matrix to mark rows and columns with zero
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0  # Only mark the cells in first row and first column
        # Iterate through matrix to update the cell to be zero if it is in a zero row or column
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        # Update the first row and column if they are zero
        if zeroFirstRow:
            for j in range(n):
                matrix[0][j] = 0
        if zeroFirstCol:
            for i in range(m):
                matrix[i][0] = 0
