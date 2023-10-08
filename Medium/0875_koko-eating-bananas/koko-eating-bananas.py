class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            mid = (l + r) // 2
            if sum((p - 1) // mid + 1 for p in piles) > h:  # (p - 1) // mid + 1 equals to math.ceil(p / mid)
                l = mid + 1
            else:
                r = mid
        return l
