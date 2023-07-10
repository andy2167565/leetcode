class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        import heapq, functools
        heapq.heapify(nums)
        for _ in range(k):  # Keep on incrementing smallest number
            heapq.heappush(nums, heapq.heappop(nums) + 1)
        return functools.reduce(lambda ans, num: ans * num % (10**9 + 7), nums, 1)  # Multiply all the numbers
