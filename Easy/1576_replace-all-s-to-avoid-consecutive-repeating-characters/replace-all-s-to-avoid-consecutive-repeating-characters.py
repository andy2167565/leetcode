class Solution:
    def modifyString(self, s: str) -> str:
#======== <Solution 1> ========#
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                for c in 'abc':
                    if (not i or s[i - 1] != c) and (i + 1 == len(s) or s[i + 1] != c):
                        s[i] = c
                        break
        return ''.join(s)

#======== <Solution 2> ========#
        ans, prev = '', '?'
        for i, c in enumerate(s):
            next = s[i + 1] if i + 1 < len(s) else '?'
            prev = c if c != '?' else {'a', 'b', 'c'}.difference({prev, next}).pop()
            ans += prev
        return ans
