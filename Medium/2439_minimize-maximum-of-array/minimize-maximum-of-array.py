class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706521/java-c-python-prefix-sum-average-o-n/
        import itertools
        return max((prefix + i) // (i + 1) for i, prefix in enumerate(itertools.accumulate(nums)))
