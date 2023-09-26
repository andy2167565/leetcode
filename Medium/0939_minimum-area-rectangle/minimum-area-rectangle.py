class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
#======== <Solution 1> ========#
        ans, seen = float('inf'), set()
        for x1, y1 in points:
            for x2, y2 in seen:
                if (x1, y2) in seen and (x2, y1) in seen:  # (x1, y1), (x1, y2), (x2, y1), (x2, y2) can form a rectangle
                    area = abs(x1 - x2) * abs(y1 - y2)
                    if area and area < ans:
                        ans = area
            seen.add((x1, y1))
        return ans if ans < float('inf') else 0

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/minimum-area-rectangle/solutions/192278/python-solution-with-detailed-explanation-with-extra-chinese-explanation/
        import collections
        ps = set(map(tuple, points))
        dx = collections.defaultdict(list)  # dx[i]: All points located at x = i
        dy = collections.defaultdict(list)  # dy[i]: All points located at y = i
        for x, y in ps:
            dx[x].append(y)
            dy[y].append(x)
        ans = float('inf')
        for x1 in sorted(dx.keys()):  # Find x1 in dx
            for i in range(len(dx[x1])):  # Find y1, y2 in dx[x1]
                y1 = dx[x1][i]
                for j in range(i + 1, len(dx[x1])):
                    y2 = dx[x1][j]
                    for x2 in dy[y2]:  # Find x2 in dy[y2]
                        if x1 < x2:
                            if (x2, y1) in ps:  # Judge (x2, y1) in points
                                ans = min(ans, abs(x1 - x2) * abs(y1 - y2))
        return ans if ans < float('inf') else 0
