class Solution:
    def generateTheString(self, n: int) -> str:
        return 'b' + 'ab'[n & 1] * (n - 1)
