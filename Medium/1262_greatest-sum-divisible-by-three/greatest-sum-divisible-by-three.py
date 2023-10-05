class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]  # dp[i]: Largest sum when divided by 3 with remainder i
        for num in nums:
            for prev_sum in dp[:]:
                curr_sum = prev_sum + num
                dp[curr_sum % 3] = max(dp[curr_sum % 3], curr_sum)
        return dp[0]
