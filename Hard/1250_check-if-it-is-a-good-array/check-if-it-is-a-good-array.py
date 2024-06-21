class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        # Reference: https://leetcode.com/problems/check-if-it-is-a-good-array/solutions/419368/java-c-python-chinese-remainder-theorem/
        import functools, math
        return functools.reduce(math.gcd, nums) == 1
