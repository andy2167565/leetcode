class Solution:
    def isPalindrome(self, s: str) -> bool:
#======== <Solution 1> ========#
        ans = ''.join(i.lower() for i in s if i.isalnum())
        return ans == ans[::-1]

#======== <Solution 2> ========#
        l, r = 0, len(s) - 1
        while l < r:
            a, b = s[l].lower(), s[r].lower()
            if a.isalnum() and b.isalnum():
                if a != b:
                    return False
                l, r = l + 1, r - 1
                continue
            l, r = l + (not a.isalnum()), r - (not b.isalnum())
        return True

#======== <Solution 3> ========#
        s_alnum = list(filter(str.isalnum, s.lower()))
        mid = len(s_alnum) // 2
        for i in range(mid):
            if s_alnum[i] != s_alnum[~i]:
                return False
        return True
