class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        import itertools
        m, n, ans = len(matrix), len(matrix[0]), float('-inf')
        for comb in itertools.combinations(range(n), n - numSelect):  # Iterate each combination of columns that are not selected
            count = len(set(row for row in range(m) for col in comb if matrix[row][col]))  # Count the number of rows that have uncovered cells
            ans = max(ans, m - count)
        return ans
