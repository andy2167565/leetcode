import collections
class DetectSquares:

    def __init__(self):
        self.countPoints = collections.Counter()

    def add(self, point: List[int]) -> None:
        self.countPoints[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for (x3, y3), count in self.countPoints.items():
            if abs(x1 - x3) and abs(x1 - x3) == abs(y1 - y3):  # Try all points p3 along with p1 to form the diagonal of non-empty square
                ans += count * self.countPoints[(x1, y3)] * self.countPoints[(x3, y1)]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
