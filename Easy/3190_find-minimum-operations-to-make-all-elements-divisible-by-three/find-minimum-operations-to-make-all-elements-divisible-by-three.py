class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(bool(num % 3) for num in nums)
