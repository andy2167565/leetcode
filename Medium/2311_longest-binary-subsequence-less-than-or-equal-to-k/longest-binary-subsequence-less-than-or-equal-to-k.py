class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
# Reference: https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/solutions/2168227/java-c-python-one-pass-o-n/
#======== <Solution 1> ========#
        dp = [0]  # dp[i]: The minimum value of subsequence with length i
        for num in map(int, s):
            if dp[-1] * 2 + num <= k:  # Append a new digit to current subsequence
                dp.append(dp[-1] * 2 + num)
            for i in range(len(dp) - 1, 0, -1):  # Check previous length of subsequences for smaller value
                dp[i] = min(dp[i], dp[i - 1] * 2 + num)
        return len(dp) - 1

#======== <Solution 2> ========#
        i = 0
        while int(s[-i-1:], 2) <= k and i < min(len(s), 32):  # Get the maximum digits from the end of string
            i += 1
        return s[:-i].count('0') + i  # Pick all the remaining zeros
