class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        import collections
        counter, balloon = collections.Counter(text), collections.Counter('balloon')
        return min(counter[c] // balloon[c] for c in balloon)
