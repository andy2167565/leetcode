class Solution:
    def longestDecomposition(self, text: str) -> int:
        # Reference: https://leetcode.com/problems/longest-chunked-palindrome-decomposition/solutions/350560/java-c-python-easy-greedy-with-prove/
        ans, l, r = 0, '', ''
        for i, j in zip(text, text[::-1]):
            l, r = l + i, j + r
            if l == r:
                ans, l, r = ans + 1, '', ''
        return ans
