class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        import collections
        d = collections.defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        return all(j - i - 1 == distance[ord(c) - 97] for c, (i, j) in d.items())
