class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        dp = [1] + [0] * target  # dp[i]: The probability of i coins facing heads
        for p in prob:
            for i in range(target, -1, -1):
                dp[i] = (dp[i - 1] if i else 0) * p + dp[i] * (1 - p)
        return dp[target]
