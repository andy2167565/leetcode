class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum(abs(i - t.index(c)) for i, c in enumerate(s))
