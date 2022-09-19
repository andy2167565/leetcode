class Solution:
    def longestNiceSubstring(self, s: str) -> str:
#======== <Solution 1> ========#
        ans = ''
        for l in range(1, len(s) + 1):
            for i in range(len(s) - l + 1):
                part = s[i: i + l]
                if all(c.swapcase() in part for c in part):
                    ans = max(ans, part, key=len)
        return ans

#======== <Solution 2> ========#
        if len(s) < 2: return ''
        for i, c in enumerate(s):
            if c.swapcase() not in set(s):
                return max(self.longestNiceSubstring(s[:i]), self.longestNiceSubstring(s[i+1:]), key=len)
        return s

#======== <Solution 3> ========#
        import re
        alone = set(s) - set(s.swapcase())
        if not alone: return s
        parts = re.split(f'[{"".join(alone)}]', s)
        return max(map(self.longestNiceSubstring, parts), key=len)
