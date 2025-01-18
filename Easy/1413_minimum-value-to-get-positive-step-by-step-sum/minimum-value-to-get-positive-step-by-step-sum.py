class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        import itertools
        return 1 - min(itertools.accumulate(nums, initial=0))
