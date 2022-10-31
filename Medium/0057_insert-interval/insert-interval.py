class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
# Reference: https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions
#======== <Solution 1> ========#
        start, end = newInterval[0], newInterval[1]
        # Collect the intervals strictly left or right of the new interval
        left = [i for i in intervals if i[1] < start]
        right = [i for i in intervals if i[0] > end]
        # Overlapping intervals exist
        if left + right != intervals:
            start = min(start, intervals[len(left)][0])
            end = max(end, intervals[~len(right)][1])
        return left + [[start, end]] + right

#======== <Solution 2> ========#
        start, end = newInterval[0], newInterval[1]
        parts = overlap, left, right = [], [], []  # parts = (overlap=[], left=[], right=[])
        # i[1] < start: left = parts[1]
        # i[0] > end: right = parts[-1]
        # start <= i[1] and i[0] <= end: overlap = parts[0]
        for i in intervals:
            parts[(i[1] < start) - (i[0] > end)].append(i)
        if overlap:
            start = min(start, overlap[0][0])
            end = max(end, overlap[-1][1])
        return left + [[start, end]] + right

#======== <Solution 3> ========#
        start, end = newInterval[0], newInterval[1]
        left, right = [], []
        for i in intervals:
            if i[1] < start:
                left += i,
            elif i[0] > end:
                right += i,
            else:
                start = min(start, i[0])
                end = max(end, i[1])
        return left + [[start, end]] + right
