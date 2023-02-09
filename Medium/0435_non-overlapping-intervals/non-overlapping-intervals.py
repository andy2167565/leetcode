class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/non-overlapping-intervals/solutions/276056/python-greedy-interval-scheduling/
        prev_end, ans = float('-inf'), 0
        for start, end in sorted(intervals, key=lambda i: i[1]):  # Always pick the interval with the earliest end time to get the maximal number of non-overlapping intervals
            if prev_end <= start:  # Non-overlapping
                prev_end = end
            else:  # Overlapping
                ans += 1
        return ans
