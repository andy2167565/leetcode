class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        heap, ans, last = [], [], 0
        for et, pt, idx in sorted((et, pt, idx) for idx, (et, pt) in enumerate(tasks)):  # Sort by enqueueTime
            while heap and last < et:
                p, i, e = heapq.heappop(heap)
                last = max(e, last) + p
                ans.append(i)
            heapq.heappush(heap, (pt, idx, et))
        while heap:  # Process remaining tasks
            ans.append(heapq.heappop(heap)[1])
        return ans
