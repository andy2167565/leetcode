class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False, False, False, True]  # dp[i % 4]: nums[:i + 1] is a valid partition
        for i in range(len(nums)):
            dp[i % 4] = False
            if i - 1 >= 0 and nums[i] == nums[i - 1]:  # Check for 2 equal elements
                dp[i % 4] |= dp[(i - 2) % 4]
            if i - 2 >= 0 and nums[i] == nums[i - 1] == nums[i - 2]:  # Check for 3 equal elements
                dp[i % 4] |= dp[(i - 3) % 4]
            if i - 2 >= 0 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:  # Check for 3 consecutive increasing elements
                dp[i % 4] |= dp[(i - 3) % 4]
        return dp[(len(nums) - 1) % 4]
