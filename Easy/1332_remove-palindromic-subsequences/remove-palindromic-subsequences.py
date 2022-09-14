class Solution:
    def removePalindromeSub(self, s: str) -> int:
#======== <Solution 1> ========#
        return 2 - (s == s[::-1])

#======== <Solution 2> ========#
        return 2 - all(s[i] == s[~i] for i in range(len(s) // 2))
