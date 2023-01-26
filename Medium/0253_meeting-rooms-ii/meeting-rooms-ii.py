class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import heapq
        intervals.sort()  # Sort by start time
        heap = []  # Store the end time of intervals increasingly
        for start, end in intervals:
            if heap and heap[0] <= start:  # If the new start time is greater than or equal to the smallest existing end time, it indicates that the room has been released. Replace the previous time with the new end time
                heapq.heapreplace(heap, end)
            else:  # The room is still in use, add (push a new end time to min heap) a new room
                heapq.heappush(heap, end)
        return len(heap)

#======== <Solution 2> ========#
        starts = sorted(start for start, _ in intervals)
        ends = sorted(end for _, end in intervals)
        i = ans = 0  # Only track the earliest end time to check the vacancy of this room
        for start in starts:
            if start < ends[i]:  # There is no vacant room, add one more room
                ans += 1
            else:  # The room with the earliest end time is vacant, assign current start time to this room and extend the interval with next end time
                i += 1
        return ans
