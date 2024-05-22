class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [0] * n  # dp[i]: The best score difference within stones[:i + 1]
        for i in range(n - 2, -1, -1):
            total = stones[i]
            for j in range(i + 1, n):
                total += stones[j]
                dp[j] = max(total - stones[i] - dp[j], total - stones[j] - dp[j - 1])
        return dp[-1]
