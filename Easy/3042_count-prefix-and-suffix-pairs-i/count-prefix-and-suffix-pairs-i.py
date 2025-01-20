class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        import itertools
        return sum(j.startswith(i) and j.endswith(i) for i, j in itertools.combinations(words, 2))
