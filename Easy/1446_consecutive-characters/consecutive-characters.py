class Solution:
    def maxPower(self, s: str) -> int:
        import itertools
        return max(len(list(g)) for _, g in itertools.groupby(s))
