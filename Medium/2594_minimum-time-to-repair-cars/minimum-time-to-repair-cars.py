class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
# Reference: https://leetcode.com/problems/minimum-time-to-repair-cars/solutions/3312003/java-c-python-binary-search-and-heap-solution/
#======== <Solution 1> ========#
        import collections, math
        counter = collections.Counter(ranks)
        l, r = 1, min(counter) * cars * cars
        while l < r:
            mid = (l + r) // 2
            if sum(math.isqrt(mid // rank) * count for rank, count in counter.items()) < cars:
                l = mid + 1
            else:
                r = mid
        return l

#======== <Solution 2> ========#
        import bisect, math
        return bisect.bisect_left(range(max(ranks) * cars * cars), cars, key=lambda time: sum(math.isqrt(time // rank) for rank in ranks))
