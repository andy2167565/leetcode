class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        import itertools
        return sum(a + b < target for a, b in itertools.combinations(nums, 2))
