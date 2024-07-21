class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        import heapq
        heap = [-abs(num1 - num2) for num1, num2 in zip(nums1, nums2)]
        delta = k1 + k2
        if delta >= -sum(heap):  # All the differences between nums1 and nums2 can be reduced to 0
            return 0
        heapq.heapify(heap)
        while delta:  # Greedily decrease the maximum difference between nums1 and nums2 until k1 + k2 becomes 0
            gap = max(delta // len(nums1), 1)
            heapq.heappush(heap, -(-heapq.heappop(heap) - gap))
            delta -= gap
        return sum(diff**2 for diff in heap)
