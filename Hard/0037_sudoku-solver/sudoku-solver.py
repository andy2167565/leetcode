class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def isValid(row, col, num):
            return not any(board[row][i] == num or board[i][col] == num or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num for i in range(9))

        def solve(row, col):
            if row == 9:  # All cells are filled
                return True
            if col == 9:  # Current row has finished
                return solve(row + 1, 0)
            if board[row][col] != '.':  # Current cell is not empty
                return solve(row, col + 1)
            for num in '123456789':  # Check the validity of each number
                if isValid(row, col, num):
                    board[row][col] = num  # Fill current cell with num
                    if solve(row, col + 1):  # Check if num is the solution
                        return True
                    board[row][col] = '.'  # If not then restore for next number
            return False

        solve(0, 0)
