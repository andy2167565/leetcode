class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
# Reference: https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach/
#======== <Solution 1> ========#
        m, n, max_side = len(matrix), len(matrix[0]), 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # Additional row and column to facilitate computing dp cells for first row and first column in matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1  # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[i + 1][j + 1])
        return max_side * max_side

#======== <Solution 2> ========#
        m, n, max_side = len(matrix), len(matrix[0]), 0
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
                if i and j and matrix[i][j]:
                    matrix[i][j] = min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i][j - 1]) + 1
                max_side = max(max_side, matrix[i][j])
        return max_side * max_side
