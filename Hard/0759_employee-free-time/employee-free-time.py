"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Reference: https://leetcode.com/problems/employee-free-time/solutions/170551/simple-python-9-liner-beats-97-with-explanation/
        intervals = sorted([interval for employee in schedule for interval in employee], key=lambda i: i.start)  # Flatten and sort the schedule by starting time
        ans, prev_end = [], intervals[0].end
        for curr in intervals[1:]:
            if prev_end < curr.start:  # Non-overlapping intervals
                ans.append(Interval(prev_end, curr.start))
            prev_end = max(prev_end, curr.end)  # Merge current interval and proceed to next one
        return ans
