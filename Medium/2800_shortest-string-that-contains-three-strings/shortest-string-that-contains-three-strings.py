class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        import itertools
        def merge(s1, s2):
            if s2 in s1:
                return s1
            for i in range(len(s1)):
                if s2.startswith(s1[i:]):  # The tail of s1 matches the head of s2
                    return s1[:i] + s2
            return s1 + s2

        ans = 'a' * 301
        for i, j, k in itertools.permutations([a, b, c]):  # Try all possibilities
            ans = min(sorted([ans, merge(merge(i, j), k)]), key=len)
        return ans
