class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # Reference: https://leetcode.com/problems/distinct-echo-substrings/solutions/477643/rolling-equality-counter/
        n, echo = len(text), set()
        text += '.'
        for l in range(1, n // 2 + 1):
            same = sum(c1 == c2 for c1, c2 in zip(text, text[l: 2 * l]))  # Check how many characters are the same between two adjacent sliding windows with length equal to l
            for i in range(n - 2 * l + 1):
                if same == l:
                    echo.add(text[i: i + l])
                same += (text[i + l] == text[i + 2 * l]) - (text[i] == text[i + l])  # Move two sliding windows one step forward
        return len(echo)
