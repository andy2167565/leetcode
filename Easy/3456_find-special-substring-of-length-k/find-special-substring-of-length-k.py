class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        import itertools
        return any(len(list(g)) == k for _, g in itertools.groupby(s))
