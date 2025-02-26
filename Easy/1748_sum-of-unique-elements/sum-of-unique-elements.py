class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        import collections
        return sum(num for num, count in collections.Counter(nums).items() if count == 1)
