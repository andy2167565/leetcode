class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = min(time), min(time) * totalTrips  # Need at least min(time) to complete a trip, and the worst case is to only use the fastest bus to complete all trips
        while l < r:
            mid = (l + r) // 2
            if sum(mid // t for t in time) < totalTrips:  # Search for larger time if not enough tasks can be completed within mid
                l = mid + 1
            else:  # Search for smaller time if enough tasks can be completed within mid
                r = mid
        return l
