class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
#======== <Solution 1> ========#
        N = len(s)
        for i in range(1, N // 2 + 1):
            if not N % i and s[:i] * (N // i) == s:
                return True
        return False

#======== <Solution 2> ========#
        return any(s[:i] * (len(s) // i) == s for i in range(1, len(s) // 2 + 1))

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/repeated-substring-pattern/discuss/826151/Python-by-fold-and-find-w-Simple-proof
        return s in (2 * s)[1:-1]

#======== <Solution 4> ========#
        # Reference 1: https://leetcode.com/problems/repeated-substring-pattern/discuss/1694256/Java-KMP-solution-with-explanation
        # Reference 2: https://leetcode.com/problems/repeated-substring-pattern/discuss/2431263/Yet-another-linear-O(n)-Python-solution-with-KMP
        border, prefix = 0, [0] * len(s)
        for i in range(1, len(s)):
            while border and s[i] != s[border]:
                border = prefix[border - 1]
            border += s[i] == s[border]
            prefix[i] = border
        return border and s.startswith(s[border:])
