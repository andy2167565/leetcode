class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/solutions/502703/clean-python-3-count-bits-in-2-lines/
        return bin(num).count('1') - 1 + len(bin(num)) - 2
