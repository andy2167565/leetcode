class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        cluster, prev_end = 0, -1
        for start, end in sorted(ranges):
            cluster += prev_end < start  # Add a new cluster if current range does not overlap with previous one
            prev_end = max(prev_end, end)
        return pow(2, cluster, 10 ** 9 + 7)  # For each cluster, there are 2 options: put it into group 1 or group 2
