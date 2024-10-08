class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        import collections
        return [num for num, count in collections.Counter(nums).items() if count == 2]
