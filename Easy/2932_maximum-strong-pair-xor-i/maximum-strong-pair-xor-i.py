class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        import itertools
        return max((x ^ y for x, y in itertools.combinations(nums, 2) if abs(x - y) <= min(x, y)), default=0)
