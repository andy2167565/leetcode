class Solution:
    def appealSum(self, s: str) -> int:
        # Reference: https://leetcode.com/problems/total-appeal-of-a-string/solutions/1999226/Combinatorics/
        import collections
        ans, n, prev = 0, len(s), collections.defaultdict(lambda: -1)
        for i, c in enumerate(s):
            ans += (i - prev[c]) * (n - i)
            prev[c] = i
        return ans
