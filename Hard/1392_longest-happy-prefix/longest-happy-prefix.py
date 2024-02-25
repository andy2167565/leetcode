class Solution:
    def longestPrefix(self, s: str) -> str:
        # Reference: https://leetcode.com/problems/longest-happy-prefix/solutions/547237/java-python-rolling-hash/
        ans = prefix = suffix = 0
        mod = 10**9 + 7
        for i in range(len(s) - 1):
            prefix = (prefix * 128 + ord(s[i])) % mod
            suffix = (suffix + pow(128, i, mod) * ord(s[~i])) % mod
            if prefix == suffix:
                ans = i + 1
        return s[:ans]
