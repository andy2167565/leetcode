class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = ans = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i] + curr * (nums[i - 1] < nums[i])
            ans = max(ans, curr)
        return ans
