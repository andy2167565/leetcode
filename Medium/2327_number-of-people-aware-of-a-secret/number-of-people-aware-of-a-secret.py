class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-people-aware-of-a-secret/solutions/2229982/java-c-python-sliding-window-o-n-time-o-forget-space/
        dp = [1] + [0] * forget  # dp[i]: The number of people who found the secret on the i-th day
        share = 0  # The number of people who are going to share the secret
        mod = 10**9 + 7
        for i in range(1, n):
            dp[i % forget] = share = (share + dp[(i - delay) % forget] - dp[i % forget]) % mod
        return sum(dp) % mod
