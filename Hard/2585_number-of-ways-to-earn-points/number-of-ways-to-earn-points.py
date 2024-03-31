class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/number-of-ways-to-earn-points/solutions/3258120/java-c-python-knapsack-dp/
        dp = [1] + [0] * target  # dp[i]: The ways to reach i points
        for count, mark in types:
            for i in range(target, -1, -1):
                for k in range(1, min(count, i // mark) + 1):
                    dp[i] = (dp[i] + dp[i - mark * k]) % (10**9 + 7)
        return dp[-1]
