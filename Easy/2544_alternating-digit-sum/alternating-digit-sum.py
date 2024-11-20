class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans, sign = 0, 1
        for num in map(int, str(n)):
            ans += num * sign
            sign *= -1
        return ans
