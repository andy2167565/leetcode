class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        def cmp(a, b):
            return (a > b) - (a < b)
        ans, [i, j], [x, y] = 0, startPos, homePos
        while i != x:
            i += cmp(x, i)
            ans += rowCosts[i]
        while j != y:
            j += cmp(y, j)
            ans += colCosts[j]
        return ans
