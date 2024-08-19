class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # Reference: https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/solutions/128952/java-c-python-one-pass-o-n/
        import collections
        ans, index = 0, collections.defaultdict(lambda: (-1, -1))
        for i, c in enumerate(s):
            second_prev, prev = index[c]  # Track indices of last two occurrences
            ans += (i - prev) * (prev - second_prev)
            index[c] = (prev, i)
        for second_prev, prev in index.values():
            ans += (len(s) - prev) * (prev - second_prev)
        return ans
