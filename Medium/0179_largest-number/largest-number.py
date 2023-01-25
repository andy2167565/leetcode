class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Reference: https://leetcode.com/problems/largest-number/solutions/213599/thinking-process-in-python/
        # Reference (Explanation): https://docs.python.org/3/library/functools.html#functools.cmp_to_key
        import functools
        # cmp_to_key: A comparison function is any callable that accepts two arguments, compares them, and returns a negative number for less-than (increasing), zero for equality, or a positive number for greater-than (decreasing)
        # Sort nums decreasingly while considering that a is larger than b if a + b > b + a (the sign of the result is negative)
        # e.g. a = '3', b = '30', a + b = '330' > '303' = b + a
        return ''.join(sorted(map(str, nums), key=functools.cmp_to_key(lambda a, b: int(b + a) - int(a + b)))).lstrip('0') or '0'  # An empty string after removing leading 0s indicates that nums only contains 0s
