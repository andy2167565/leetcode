class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        import collections, math
        return sum(math.comb(count, 2) for count in collections.Counter(nums).values())
