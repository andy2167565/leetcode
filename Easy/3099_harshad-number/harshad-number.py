class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        ans = sum(map(int, str(x)))
        return ans if not x % ans else -1
