class Solution:
    def matrixSumQueries(self, n: int, queries: List[List[int]]) -> int:
        ans, rows, cols = 0, set(), set()  # Store the indices of filled rows and columns
        for t, i, v in queries[::-1]:  # The queries that come later have a greater impact on the final sum
            if t and i not in cols:  # Fill column
                cols.add(i)
                ans += v * (n - len(rows))  # Ignore filled rows
            elif not t and i not in rows:  # Fill row
                rows.add(i)
                ans += v * (n - len(cols))  # Ignore filled columns
        return ans
