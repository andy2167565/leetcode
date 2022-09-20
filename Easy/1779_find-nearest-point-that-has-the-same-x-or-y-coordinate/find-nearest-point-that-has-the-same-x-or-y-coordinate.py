class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
#======== <Solution 1> ========#
        dist, ans = float('inf'), -1
        for i, point in enumerate(points):
            dx, dy = abs(point[0] - x), abs(point[1] - y)
            if not dx * dy and dx + dy < dist:
                dist, ans = dx + dy, i
        return ans

#======== <Solution 2> ========#
        points.append([float('inf'), float('inf')])
        dist = lambda point: abs(point[0] - x) + abs(point[1] - y)
        ans = -1
        for i, point in enumerate(points):
            if (point[0] == x or point[1] == y) and dist(point) < dist(points[ans]):
                ans = i
        return ans
