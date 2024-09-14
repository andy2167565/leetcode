class Solution:
    def averageValue(self, nums: List[int]) -> int:
        arr = [num for num in nums if not num % 6]
        return sum(arr) // len(arr) if arr else 0
