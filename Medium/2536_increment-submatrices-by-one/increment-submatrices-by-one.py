class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
#======== <Solution 1> ========#
        import numpy as np
        mat = np.array([[0] * n for _ in range(n)])
        for row1, col1, row2, col2 in queries:
            mat[row1: row2 + 1, col1: col2 + 1] += 1
        return mat

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/increment-submatrices-by-one/solutions/3052675/python3-sweep-line-range-addition-clean-concise/
        mat = [[0] * n for _ in range(n)]
        for r1, c1, r2, c2 in queries:
            for r in range(r1, r2 + 1):
                mat[r][c1] += 1  # Only add c1 by 1 for each row
                if c2 + 1 < n:  # c2 is not the last column of the matrix
                    mat[r][c2 + 1] -= 1  # Subtract 1 from the next column of c2 to cancel out the addition in later process
        for r in range(n):
            for c in range(1, n):
                mat[r][c] += mat[r][c - 1]  # Prefix sum from previous column
        return mat
