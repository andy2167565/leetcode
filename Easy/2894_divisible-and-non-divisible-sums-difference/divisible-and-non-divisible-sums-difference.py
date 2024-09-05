class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # Reference: https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/solutions/4143950/java-c-python-math/
        return (1 + n) * n // 2 - (1 + n // m) * (n // m) * m
