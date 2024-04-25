class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        import sys
        sys.set_int_max_str_digits(5000)
        dp = [0] + [-1] * (target + 5000)  # dp[i]: The maximum integer with cost i
        for curr in range(1, target + 1):
            dp[curr] = max(dp[curr - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[target], 0))
