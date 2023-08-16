class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            freqs = [0] * 26  # Initialize a new frequency array for each substring
            for j in range(i, len(s)):
                freqs[ord(s[j]) - 97] += 1
                ans += max(freqs) - min(freq for freq in freqs if freq)
        return ans
