class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        import functools, operator
        return functools.reduce(operator.xor, arr1) & functools.reduce(operator.xor, arr2)  # (a1 ^ a2) & (b1 ^ b2) = (a1 & b1) ^ (a1 & b2) ^ (a2 & b1) ^ (a2 & b2)
