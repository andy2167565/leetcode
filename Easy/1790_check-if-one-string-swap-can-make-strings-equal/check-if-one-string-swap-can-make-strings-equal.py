class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [(c1, c2) for c1, c2 in zip(s1, s2) if c1 != c2]
        return not diff or (len(diff) == 2 and diff[0][::-1] == diff[1])
