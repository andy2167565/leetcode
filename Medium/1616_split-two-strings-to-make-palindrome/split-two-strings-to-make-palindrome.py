class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def check(a, b):
            i, j = 0, len(a) - 1
            while i < j and a[i] == b[j]:  # a_prefix = reversed(b_suffix)
                i += 1
                j -= 1
            return a[i: j + 1], b[i: j + 1]  # Return the middle parts
        return any(s == s[::-1] for s in check(a, b) + check(b, a))
