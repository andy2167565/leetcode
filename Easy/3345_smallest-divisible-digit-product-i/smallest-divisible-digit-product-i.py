class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        import functools, operator
        for i in range(n, n + 10):
            if not functools.reduce(operator.mul, map(int, str(i))) % t:
                return i
