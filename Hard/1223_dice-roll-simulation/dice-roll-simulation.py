class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        dp = [[0] * (faces + 1) for _ in range(n + 1)]  # dp[i][j]: The number of combinations at i-th rolling ending with face j
        dp[0][-1] = 1  # Roll 0 time, the total combination is 1
        for j in range(faces):  # Roll 1 time, the combinations that end with face j is 1
            dp[1][j] = 1
        dp[1][-1] = faces  # Roll 1 time, the total combination is faces = 6
        for i in range(2, n + 1):  # Roll dices from 2 times to n times
            for j in range(faces):  # Iterate through each column (face)
                for k in range(1, rollMax[j] + 1):  # At each (i, j), try to go up (decrease i) and collect all the sum of previous states
                    if i - k < 0:
                        break
                    dp[i][j] += dp[i - k][-1] - dp[i - k][j]
            dp[i][-1] = sum(dp[i])  # Update total sum of current row
        return dp[-1][-1] % (10**9 + 7)
