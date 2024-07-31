class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/solutions/4671722/sort-and-track-max-y/
        ans = 0
        points.sort(key=lambda p: (p[0], -p[1]))  # Sorted from the upper left to the lower right
        for i, (x1, y1) in enumerate(points):
            y = float('-inf')  # Track the largest y so far
            for (x2, y2) in points[i + 1:]:
                if y1 >= y2 > y:
                    ans += 1
                    y = y2
        return ans
