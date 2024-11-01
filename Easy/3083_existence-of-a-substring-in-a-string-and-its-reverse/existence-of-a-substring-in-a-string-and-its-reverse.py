class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        import itertools
        return bool(set(itertools.pairwise(s)) & set(itertools.pairwise(s[::-1])))
