class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)  # dp[i]: The result for n = i
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))  # The other competitor will lose the game if dp[i - k * k] == False
        return dp[-1]
