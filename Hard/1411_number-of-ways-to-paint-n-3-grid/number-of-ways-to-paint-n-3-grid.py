class Solution:
    def numOfWays(self, n: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/solutions/574923/java-c-python-dp-o-1-space/
        pattern_121 = pattern_123 = 6
        for _ in range(n - 1):
            pattern_121, pattern_123 = pattern_121 * 3 + pattern_123 * 2, pattern_121 * 2 + pattern_123 * 2
        return (pattern_121 + pattern_123) % (10**9 + 7)
