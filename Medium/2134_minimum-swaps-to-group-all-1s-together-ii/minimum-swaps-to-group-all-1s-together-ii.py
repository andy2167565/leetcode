class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones, n = nums.count(1), len(nums)
        curr_ones = max_ones = 0  # Maximum number of ones seen in the window
        for i in range(n * 2):
            if i >= total_ones and nums[i % n - total_ones]:  # Move the window forward
                curr_ones -= 1
            if nums[i % n] == 1:
                curr_ones += 1
            max_ones = max(max_ones, curr_ones)
        return total_ones - max_ones
