class Solution:
    def pivotInteger(self, n: int) -> int:
        import math
        num = math.sqrt(n * (n + 1) // 2)
        return int(num) if not num - math.ceil(num) else -1
