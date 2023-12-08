class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq
        maxheap = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]  # Sorted by the delta when adding one extra student for each class
        heapq.heapify(maxheap)
        while extraStudents:
            _, p, t = heapq.heappop(maxheap)
            p, t = p + 1, t + 1
            heapq.heappush(maxheap, (p / t - (p + 1) / (t + 1), p, t))
            extraStudents -= 1
        return sum(p / t for _, p, t in maxheap) / len(maxheap)
