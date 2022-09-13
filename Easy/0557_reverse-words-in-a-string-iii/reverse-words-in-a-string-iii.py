class Solution:
    def reverseWords(self, s: str) -> str:
#======== <Solution 1> ========#
        return ' '.join(word[::-1] for word in s.split())

#======== <Solution 2> ========#
        return ' '.join(s.split()[::-1])[::-1]

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/reverse-words-in-a-string-iii/discuss/1051657/Python-3%3A-Two-pointer-approach-(for-the-sake-of-practice)
        l, r = 0, 0
        while r < len(s):
            while r < len(s) and s[r] != ' ':
                r += 1
            s = s[:l] + s[l:r][::-1] + s[r:]
            r += 1
            l = r
        return s
