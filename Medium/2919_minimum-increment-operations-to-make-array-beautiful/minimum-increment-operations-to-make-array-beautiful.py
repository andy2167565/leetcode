class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/solutions/4220717/java-c-python-dp-o-1-space/
        dp1 = dp2 = dp3 = 0  # dp[i]: Number of operations to increment nums[i - 3], nums[i - 2], nums[i - 1] to k respectively
        for num in nums:
            dp1, dp2, dp3 = dp2, dp3, min(dp1, dp2, dp3) + max(k - num, 0)
        return min(dp1, dp2, dp3)
