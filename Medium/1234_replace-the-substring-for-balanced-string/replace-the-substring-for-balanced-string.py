class Solution:
    def balancedString(self, s: str) -> int:
        # Reference: https://leetcode.com/problems/replace-the-substring-for-balanced-string/solutions/408978/java-c-python-sliding-window/
        import collections
        ans = n = len(s)
        i, counter = 0, collections.Counter(s)
        for j, c in enumerate(s):
            counter[c] -= 1
            while i < n and all(counter[c] <= n / 4 for c in 'QWER'):
                if i > j:
                    return 0
                ans = min(ans, j - i + 1)
                counter[s[i]] += 1
                i += 1
        return ans
