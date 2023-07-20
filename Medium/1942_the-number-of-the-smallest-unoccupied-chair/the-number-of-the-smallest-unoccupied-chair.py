class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        import heapq
        available, leave_times = list(range(len(times))), []
        for arrival, leaving in sorted(times):
            while leave_times and leave_times[0][0] <= arrival:  # Previous friends have released empty chairs
                heapq.heappush(available, heapq.heappop(leave_times)[1])
            if arrival == times[targetFriend][0]:  # targetFriend has arrived
                return available[0]
            heapq.heappush(leave_times, (leaving, heapq.heappop(available)))
