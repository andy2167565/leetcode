class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        import itertools
        return all(len(list(g)) <= 2 for _, g in itertools.groupby(sorted(nums)))
