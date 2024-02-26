class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175090/java-c-python-sliding-window/
        l = 0
        nums.sort()
        for r, num in enumerate(nums):
            k += num
            if k < num * (r - l + 1):  # Check if the sum can fill the window evenly
                k -= nums[l]
                l += 1
        return r - l + 1
