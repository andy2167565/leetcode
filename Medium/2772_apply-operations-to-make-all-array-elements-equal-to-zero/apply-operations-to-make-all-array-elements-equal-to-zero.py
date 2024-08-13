class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        # Reference: https://leetcode.com/problems/apply-operations-to-make-all-array-elements-equal-to-zero/solutions/3739101/java-c-python-greedy-sliding-window/
        curr = 0  # Sum of previous (k - 1) elements
        for i, num in enumerate(nums):
            if curr > num:
                return False
            nums[i], curr = num - curr, num
            if i >= k - 1:
                curr -= nums[i - k + 1]
        return not curr
