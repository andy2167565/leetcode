class Solution:
    def replaceDigits(self, s: str) -> str:
#======== <Solution 1> ========#
        for i in range(1, len(s), 2):
            s = s.replace(s[i], chr(ord(s[i-1]) + int(s[i])), 1)
        return s

#======== <Solution 2> ========#
        return ''.join(chr(ord(s[i-1]) + int(s[i])) if i % 2 else s[i] for i in range(len(s)))
