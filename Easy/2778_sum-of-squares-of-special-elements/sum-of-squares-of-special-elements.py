class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(num**2 for i, num in enumerate(nums, 1) if not len(nums) % i)
