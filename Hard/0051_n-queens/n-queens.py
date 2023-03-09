class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Reference: https://leetcode.com/problems/n-queens/solutions/19810/fast-short-and-easy-to-understand-python-solution-11-lines-76ms/
        def dfs(queens=[], rc_dif=[], rc_sum=[]):  # e.g. queens = [1, 3, 0, 2] indicates that the first queen is placed in column 1, the second queen is placed in column 3, etc.
            r = len(queens)  # Get current row number
            if r == n:  # A solution has been completed
                return [['.' * c + 'Q' + '.' * (n - c - 1) for c in queens]]
            solutions = []
            for c in range(n):  # Iterate all columns in current row
                if c not in queens and r - c not in rc_dif and r + c not in rc_sum:  # If a location (row, col) is occupied, any other locations (r, c) where r - c == row - col or r + c == row + col would be invalid, i.e. diagonal locations
                    solutions += dfs(queens + [c], rc_dif + [r - c], rc_sum + [r + c])
            return solutions
        return dfs()
