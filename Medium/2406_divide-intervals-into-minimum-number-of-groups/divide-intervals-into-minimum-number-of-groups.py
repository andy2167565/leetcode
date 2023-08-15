class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        import heapq
        pq = []  # Store the rightmost index of each group
        for l, r in sorted(intervals):
            if pq and pq[0] < l:  # Put current interval in an existing group
                heapq.heappop(pq)
            heapq.heappush(pq, r)
        return len(pq)
