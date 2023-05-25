class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/max-consecutive-ones-iii/solutions/247564/java-c-python-sliding-window/
        l = 0
        for r in range(len(nums)):
            k -= 1 - nums[r]
            if k < 0:  # There are more than k zeros in sliding window
                k += 1 - nums[l]
                l += 1
        return r - l + 1
