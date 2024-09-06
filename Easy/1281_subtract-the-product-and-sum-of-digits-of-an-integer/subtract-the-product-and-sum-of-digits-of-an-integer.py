class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        import math
        digits = list(map(int, str(n)))
        return math.prod(digits) - sum(digits)
