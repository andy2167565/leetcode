class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
#======== <Solution 1> ========#
        leftover = money - sum(sorted(prices)[:2])
        return leftover if leftover >= 0 else money

#======== <Solution 2> ========#
        import heapq
        heapq.heapify(prices)
        leftover = money - sum(heapq.nsmallest(2, prices))
        return leftover if leftover >= 0 else money

#======== <Solution 3> ========#
        min1 = min2 = float('inf')
        for p in prices:
            if p < min1:
                min2, min1 = min1, p
            elif p < min2:
                min2 = p
        leftover = money - min1 - min2
        return leftover if leftover >= 0 else money
