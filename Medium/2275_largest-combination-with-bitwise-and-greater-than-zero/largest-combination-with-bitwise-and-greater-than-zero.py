class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Reference: https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/solutions/2039903/java-c-python-bit-solution/
        return max(sum(1 << i & num > 0 for num in candidates) for i in range(24))  # 10^7 < 2^24 = 16777216
