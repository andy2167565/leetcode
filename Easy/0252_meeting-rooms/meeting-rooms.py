class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
#======== <Solution 1> ========#
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True

#======== <Solution 2> ========#
        intervals.sort()
        return all(i[1] <= j[0] for i, j in zip(intervals, intervals[1:]))
