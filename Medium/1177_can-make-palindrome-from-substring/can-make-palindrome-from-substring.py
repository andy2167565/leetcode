class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
# Reference: https://leetcode.com/problems/can-make-palindrome-from-substring/solutions/371849/java-python-3-3-codes-each-prefix-sum-boolean-and-xor-of-characters-frequencies-then-compare/
#======== <Solution 1> ========#
        dp = [[0] * 26]  # dp[i]: The counts of each letter in s[:i]
        for i, c in enumerate(s):
            dp.append(dp[i][:])
            dp[i + 1][ord(c) - ord('a')] += 1
        return [sum((dp[r + 1][i] - dp[l][i]) % 2 for i in range(26)) // 2 <= k for l, r, k in queries]  # Sum the letters with odd count and only need to replace half of them

#======== <Solution 2> ========#
        dp = [[False] * 26]  # dp[i]: The count is odd or not for each letter in s[:i]
        for i, c in enumerate(s):
            dp.append(dp[i][:])
            dp[i + 1][ord(c) - ord('a')] ^= True
        return [sum(dp[r + 1][i] ^ dp[l][i] for i in range(26)) // 2 <= k for l, r, k in queries]

#======== <Solution 3> ========#
        dp = [0]  # dp[i]: The counts of each letter in s[:i] represented by binary digit e.g. 1110 indicates that b, c, d are odds while a is even
        for i, c in enumerate(s):
            dp.append(dp[i] ^ 1 << (ord(c) - ord('a')))
        return [bin(dp[r + 1] ^ dp[l]).count('1') // 2 <= k for l, r, k in queries]
