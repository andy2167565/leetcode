# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # Reference: https://leetcode.com/problems/number-of-ships-in-a-rectangle/solutions/441406/python-quartered-search-and-o-1-hack-for-fun/
        ans = 0
        if topRight.x >= bottomLeft.x and topRight.y >= bottomLeft.y and sea.hasShips(topRight, bottomLeft):
            if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return 1
            mx, my = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
            ans += self.countShips(sea, topRight, Point(mx + 1, my + 1))
            ans += self.countShips(sea, Point(mx, topRight.y), Point(bottomLeft.x, my + 1))
            ans += self.countShips(sea, Point(mx, my), bottomLeft)
            ans += self.countShips(sea, Point(topRight.x, my), Point(mx + 1, bottomLeft.y))
        return ans
