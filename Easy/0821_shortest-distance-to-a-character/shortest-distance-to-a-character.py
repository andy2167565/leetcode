class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
#======== <Solution 1> ========#
        import re
        indices = [span.start() for span in re.finditer(c, s)]
        return [min(abs(i - index) for index in indices) for i in range(len(s))]

# Reference: https://leetcode.com/problems/shortest-distance-to-a-character/discuss/125788/C%2B%2BJavaPython-2-Pass-with-Explanation
#======== <Solution 2> ========#
        n, pos = len(s), -float('inf')
        ans, ls = [n] * n, tuple(range(n))
        for i in ls + ls[::-1]:
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i], abs(i - pos))
        return ans

#======== <Solution 3>: Dynamic Programming - Bottom-up Two-pass ========#
        n = len(s)
        ans = [0 if ch == c else n for ch in s]
        # Find shortest distance to character on left
        for i in range(1, n):
            ans[i] = min(ans[i], ans[i - 1] + 1)
        # Find shortest distance to character on right
        for i in reversed(range(n - 1)):
            ans[i] = min(ans[i], ans[i + 1] + 1)
        return ans
