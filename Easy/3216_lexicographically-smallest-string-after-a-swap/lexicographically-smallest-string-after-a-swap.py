class Solution:
    def getSmallestString(self, s: str) -> str:
        import itertools
        s = list(s)
        for i, j in itertools.pairwise(range(len(s))):
            if s[i] > s[j] and not (ord(s[i]) - ord(s[j])) % 2:
                s[i], s[j] = s[j], s[i]
                break
        return ''.join(s)
