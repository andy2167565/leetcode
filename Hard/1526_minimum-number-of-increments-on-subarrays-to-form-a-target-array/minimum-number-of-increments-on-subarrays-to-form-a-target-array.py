class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/solutions/754674/java-c-python-comparison-of-consecutive-elements/
        return sum(max(curr - prev, 0) for curr, prev in zip(target, [0] + target))
