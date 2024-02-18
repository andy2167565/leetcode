class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/maximum-earnings-from-taxi/solutions/1470935/c-python-dp-o-m-n-clean-concise/
        dp = [0] * (n + 1)  # dp[i]: The maximum dollars we can earn starting from point i
        rides.sort()
        for i in range(n - 1, 0, -1):
            dp[i] = dp[i + 1]
            while rides and i == rides[-1][0]:  # Pick up the passenger at point i
                s, e, t = rides.pop()
                dp[i] = max(dp[i], dp[e] + e - s + t)
        return dp[1]
