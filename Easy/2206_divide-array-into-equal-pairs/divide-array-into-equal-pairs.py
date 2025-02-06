class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        import collections
        return all(not count % 2 for count in collections.Counter(nums).values())
