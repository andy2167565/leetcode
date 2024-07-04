class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/solutions/1976972/python3-easy-to-understand-count-by-h/
        import collections, bisect
        ans, hashmap = [], collections.defaultdict(list)
        for l, h in rectangles:
            hashmap[h].append(l)
        for h in hashmap:
            hashmap[h].sort()
        for x, y in points:
            count = 0
            for h in range(y, 101):  # Rectangles whose h is larger than or equal to target point
                j = bisect.bisect_left(hashmap[h], x)  # Rectangles whose l is smaller than target point
                count += len(hashmap[h]) - j
            ans.append(count)
        return ans
