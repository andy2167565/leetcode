class Solution:
    def lastSubstring(self, s: str) -> str:
        # Reference: https://leetcode.com/problems/last-substring-in-lexicographical-order/solutions/363662/short-python-code-o-n-time-and-o-1-space-with-proof-and-visualization/
        i, j, offset = 0, 1, 0
        while j + offset < len(s):
            if s[i + offset] == s[j + offset]:
                offset += 1
                continue
            elif s[i + offset] < s[j + offset]:
                i += offset + 1
            else:
                j += offset + 1
            if i == j:  # Break tie
                j += 1
            offset = 0
        return s[i:]
