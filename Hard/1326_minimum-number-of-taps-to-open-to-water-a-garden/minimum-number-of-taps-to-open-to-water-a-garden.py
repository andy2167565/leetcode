class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/484235/java-c-python-similar-to-lc1024/
        dp = [0] + [n + 2] * n  # dp[i]: The minimum number of taps to water [0, i + 1]
        for i, num in enumerate(ranges):
            for j in range(max(i - num + 1, 0), min(i + num, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - num)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
