class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # Reference: https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/discuss/903611/Javascript-Combinations-explanation-%2B-visualization
        import math
        return math.comb(n + k - 1, 2 * k) % (10**9 + 7)
