class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
#======== <Solution 1> ========#
        import fractions, itertools
        ans, gradient = 0, None
        for p1, p2 in itertools.pairwise(sorted(stockPrices)):
            new_gradient = fractions.Fraction(p2[1] - p1[1], p2[0] - p1[0])
            if new_gradient != gradient:
                gradient = new_gradient
                ans += 1
        return ans

#======== <Solution 2> ========#
        import fractions, itertools
        return sum(1 for _ in itertools.groupby(fractions.Fraction(y2 - y1, x2 - x1) for (x1, y1), (x2, y2) in itertools.pairwise(sorted(stockPrices))))

#======== <Solution 3> ========#
        stockPrices.sort()
        ans = len(stockPrices) - 1
        for i in range(2, len(stockPrices)):
            (x1, y1), (x2, y2), (x3, y3) = stockPrices[i - 2], stockPrices[i - 1], stockPrices[i]
            if (y3 - y2) * (x2 - x1) == (x3 - x2) * (y2 - y1):
                ans -= 1
        return ans
