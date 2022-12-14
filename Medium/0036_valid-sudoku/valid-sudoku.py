class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
#======== <Solution 1> ========#
        return self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board)

    def is_row_valid(self, board):
        return all(self.is_unit_valid(row) for row in board)

    def is_col_valid(self, board):
        return all(self.is_unit_valid(col) for col in zip(*board))

    def is_square_valid(self, board):
        return all(self.is_unit_valid([board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]) for i in (0, 3, 6) for j in (0, 3, 6))

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']  # All digits in unit
        return len(set(unit)) == len(unit)  # A sudoku is not valid if any unit (row, column or square) contains duplicates

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/valid-sudoku/solutions/15509/clean-and-easy82ms-python/comments/174659
        seen = set()
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    curr = {(i, c), (c, j), (i//3, j//3, c)}
                    if curr & seen:
                        return False
                    seen.update(curr)
        return True
