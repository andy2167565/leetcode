class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # Reference: https://leetcode.com/problems/number-of-paths-with-max-score/solutions/463252/python-dp-solution/
        dp = [[[float('-inf'), 0] for _ in range(len(board) + 1)] for _ in range(len(board) + 1)]  # dp[i][j]: [The maximum value to current cell, The number of such paths]
        dp[-2][-2] = [0, 1]  # Starting cell
        for i in range(len(board))[::-1]:
            for j in range(len(board))[::-1]:
                if board[i][j] not in 'XS':
                    for di, dj in (0, 1), (1, 0), (1, 1):
                        if dp[i][j][0] < dp[i + di][j + dj][0]:
                            dp[i][j] = [dp[i + di][j + dj][0], 0]
                        if dp[i][j][0] == dp[i + di][j + dj][0]:
                            dp[i][j][1] += dp[i + di][j + dj][1]
                    dp[i][j][0] += int(board[i][j]) if i or j else 0
        return [dp[0][0][0] if dp[0][0][1] else 0, dp[0][0][1] % (10**9 + 7)]
