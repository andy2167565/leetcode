class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Reference: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/solutions/2948183/python-clean-12-line-sliding-window-solution-with-explanation/
        limits = {c: s.count(c) - k for c in 'abc'}  # Take at most count(c) - k of each character from middle
        if any(val < 0 for val in limits.values()):
            return -1
        counts = {c: 0 for c in 'abc'}
        ans = l = 0
        for r, c in enumerate(s):
            counts[c] += 1
            while counts[c] > limits[c]:
                counts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return len(s) - ans
