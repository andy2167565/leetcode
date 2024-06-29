class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        # Reference: https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/solutions/899511/java-python-3-bfs-and-dfs-w-brief-explanation-and-analysis/
        seen = set()

        def dfs(s):
            if s in seen:
                return s
            seen.add(s)
            add_odd = ''.join(even + str((odd + a) % 10) for even, odd in zip(s[::2], map(int, s[1::2])))
            return min(s, dfs(add_odd), dfs(s[b:] + s[:b]))

        return dfs(s)
