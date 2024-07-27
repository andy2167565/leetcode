class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/solutions/510263/java-c-python-priority-queue/
        import heapq
        events.sort(reverse=True)
        ends = []
        ans = d = 0
        while events or ends:
            if not ends:  # Start from the starting day of the next event
                d = events[-1][0]
            while events and events[-1][0] <= d:  # Collect all events that we can possibly attend
                heapq.heappush(ends, events.pop()[1])
            heapq.heappop(ends)  # Attend the event that ends the earliest
            ans += 1
            d += 1
            while ends and ends[0] < d:  # Remove all events that we cannot attend
                heapq.heappop(ends)
        return ans
