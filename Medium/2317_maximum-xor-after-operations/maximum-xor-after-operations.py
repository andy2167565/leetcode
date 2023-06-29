class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        import functools, operator
        return functools.reduce(operator.ior, nums)
