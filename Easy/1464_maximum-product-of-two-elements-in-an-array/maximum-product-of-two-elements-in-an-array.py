class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import math, heapq
        return math.prod(num - 1 for num in heapq.nlargest(2, nums))
