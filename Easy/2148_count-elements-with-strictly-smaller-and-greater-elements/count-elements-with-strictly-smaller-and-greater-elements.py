class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[0] < nums[i] < nums[len(nums) - 1] for i in range(1, len(nums) - 1))
