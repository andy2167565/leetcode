class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        import itertools
        return sum(j - i == k - j == diff for i, j, k in itertools.combinations(nums, 3))
