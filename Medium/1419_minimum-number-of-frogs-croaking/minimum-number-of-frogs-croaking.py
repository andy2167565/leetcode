class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # Reference: https://leetcode.com/problems/minimum-number-of-frogs-croaking/solutions/586653/c-python-java-lucid-code-with-documened-comments-visualization/
        c = r = o = a = k = frogs = ans = 0
        for ch in croakOfFrogs:
            if ch == 'c':  # A new frog or one of the existing frogs has started to croak
                c += 1
                frogs += 1
            elif ch == 'r':
                r += 1
            elif ch == 'o':
                o += 1
            elif ch == 'a':
                a += 1
            else:  # One of the frogs have stopped croaking
                k += 1
                frogs -= 1
            ans = max(ans, frogs)
            if c < r or r < o or o < a or a < k:
                return -1
        return ans if c == r == o == a == k else -1
