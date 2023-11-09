class Solution:
    def minimumCost(self, s: str) -> int:
        return sum(min(i, len(s) - i) for i in range(1, len(s)) if s[i] != s[i - 1])
