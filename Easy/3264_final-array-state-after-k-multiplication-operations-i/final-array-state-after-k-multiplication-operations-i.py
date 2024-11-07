class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        import heapq
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)
        while k:
            num, i = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, i))
            k -= 1
        return list(zip(*sorted(heap, key=lambda x: x[1])))[0]
