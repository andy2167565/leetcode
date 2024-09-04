class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(not len(num) % 2 for num in map(str, nums))
