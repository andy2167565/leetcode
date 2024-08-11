class Solution:
    def minimumDistance(self, word: str) -> int:
        # Reference: https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/solutions/477652/java-c-python-1d-dp-o-1-space/
        def dist(a, b):
            x1, y1 = divmod(a, 6)
            x2, y2 = divmod(b, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        dp, word = [0] * 26, [ord(c) - 65 for c in word]
        for c1, c2 in zip(word, word[1:]):
            dp[c1] = max(dp[i] + dist(c1, c2) - dist(i, c2) for i in range(26))
        return sum(dist(c1, c2) for c1, c2 in zip(word, word[1:])) - max(dp)
