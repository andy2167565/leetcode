class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26  # dp[i]: The length of the longest ideal subsequence ending with i-th character
        for c in s:
            i = ord(c) - 97
            dp[i] = max(dp[max(0, i - k): min(25, i + k) + 1]) + 1  # c can be the next character for subsequences ending from (i - k)th character to (i + k)th character
        return max(dp)
