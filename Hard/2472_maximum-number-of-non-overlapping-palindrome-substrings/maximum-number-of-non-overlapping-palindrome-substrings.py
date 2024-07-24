class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/solutions/2808805/c-java-python3-palindromic-substrings-non-overlapping-intervals/
        n, ans, start = len(s), 0, 0
        for i in range(2 * n - 1):
            l, r = i // 2, (i + 1) // 2
            while start <= l <= r < n and s[l] == s[r]:  # Find all palindromic substrings with length >= k
                if r - l + 1 >= k:
                    ans += 1
                    start = r + 1
                    break
                l -= 1
                r += 1
        return ans
