class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]  # dp[i]: Minimum side jumps to reach lane i + 1
        for lane in obstacles:
            if lane:  # Reset the jumps when encounter a stone
                dp[lane - 1] = float('inf')
            for i in range(3):
                if lane != i + 1:
                    dp[i] = min(dp[i], dp[(i + 1) % 3] + 1, dp[(i + 2) % 3] + 1)
        return min(dp)
