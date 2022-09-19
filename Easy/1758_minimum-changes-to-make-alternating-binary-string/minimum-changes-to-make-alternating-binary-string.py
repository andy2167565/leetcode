class Solution:
    def minOperations(self, s: str) -> int:
        zero_one = sum(i % 2 == int(c) for i, c in enumerate(s))
        return min(zero_one, len(s) - zero_one)
