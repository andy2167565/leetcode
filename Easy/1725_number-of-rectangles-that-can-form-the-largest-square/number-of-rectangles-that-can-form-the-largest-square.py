class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans = maxLen = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > maxLen:
                ans, maxLen = 1, side
            elif side == maxLen:
                ans += 1
        return ans
