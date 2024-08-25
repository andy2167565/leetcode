class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        import itertools
        return list(itertools.accumulate(nums)).count(0)
