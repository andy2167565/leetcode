class Solution:
    def countKeyChanges(self, s: str) -> int:
        import itertools
        return len(list(itertools.groupby(s.lower()))) - 1
