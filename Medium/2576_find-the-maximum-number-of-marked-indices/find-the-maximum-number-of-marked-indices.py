class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        ans = i = 0
        mid = j = len(nums) // 2
        nums.sort()
        while i < mid and j < len(nums):
            if 2 * nums[i] <= nums[j]:
                ans += 2
                i += 1
            j += 1
        return ans
