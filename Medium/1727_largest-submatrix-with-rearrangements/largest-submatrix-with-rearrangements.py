class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):  # Calculate heights for each column
            for j in range(n):
                if matrix[i][j]:
                    matrix[i][j] += matrix[i - 1][j]
        ans = 0
        for i in range(m):
            matrix[i].sort()  # Sort the heights in ascending order
            for j in range(n):  # Iterate through the sorted heights
                ans = max(ans, matrix[i][j] * (n - j))
        return ans
