class Solution:
    def robotWithString(self, s: str) -> str:
        # Reference: https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/solutions/2678810/counter/
        import collections
        counter, lo, t, paper = collections.Counter(s), 'a', [], []
        for c in s:
            t += c
            counter[c] -= 1
            while lo < 'z' and not counter[lo]:
                lo = chr(ord(lo) + 1)
            while t and t[-1] <= lo:
                paper += t.pop()
        return ''.join(paper)
