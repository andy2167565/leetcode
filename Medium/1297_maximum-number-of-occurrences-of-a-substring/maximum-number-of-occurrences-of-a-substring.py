class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/solutions/462213/python-2-lines-counter/
        import collections
        counter = collections.Counter(s[i:i + minSize] for i in range(len(s) - minSize + 1))  # Only collect the frequencies of substrings with minSize
        return max([counter[w] for w in counter if len(set(w)) <= maxLetters], default=0)
