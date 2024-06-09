class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        import collections
        pos1 = [(i, j) for i, row in enumerate(img1) for j, num in enumerate(row) if num]
        pos2 = [(i, j) for i, row in enumerate(img2) for j, num in enumerate(row) if num]
        counter = collections.Counter((x1 - x2, y1 - y2) for x1, y1 in pos1 for x2, y2 in pos2)
        return max(counter.values(), default=0)
