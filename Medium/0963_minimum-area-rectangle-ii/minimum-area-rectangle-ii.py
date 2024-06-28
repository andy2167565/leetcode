class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        # Reference: https://leetcode.com/problems/minimum-area-rectangle-ii/solutions/208377/python-easy-to-understand-dot-product-o-n-3-ac/
        area, point_set = float('inf'), {(x, y) for x, y in points}
        for i, (x1, y1) in enumerate(points):
            for j, (x2, y2) in enumerate(points[i + 1:], i + 1):
                for k, (x3, y3) in enumerate(points[j + 1:], j + 1):
                    if not (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) and (x3 + (x2 - x1), y3 + (y2 - y1)) in point_set:
                        area = min(area, ((x2 - x1)**2 + (y2 - y1)**2)**0.5 * ((x3 - x1)**2 + (y3 - y1)**2)**0.5)
        return area if area < float('inf') else 0
