class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Reference: https://leetcode.com/problems/minimum-window-substring/solutions/26804/12-lines-python/
        import collections
        need = collections.Counter(t)  # Frequency of chars needed
        missing = len(t)  # Number of chars to be matched
        i = start = end = 0
        for j, c in enumerate(s, 1):  # Index starting from 1 for later slicing
            missing -= need[c] > 0  # Char c has matched chars in t
            need[c] -= 1
            if not missing:  # All chars in t are matched
                while need[s[i]] < 0:  # We have included more s[i] than needed. Adjust the size of current window
                    need[s[i]] += 1
                    i += 1
                if not end or j - i < end - start:  # Update the result window
                    start, end = i, j
        return s[start:end]
