class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)  # The minimum and maximum possible weight capacities of the ship
        while l < r:
            mid = (l + r) // 2  # Current weight capacity of the ship
            need = 1  # Days needed to ship all the packages
            curr = 0  # Current weight in the ship
            for weight in weights:
                if curr + weight > mid:
                    need += 1
                    curr = 0
                curr += weight
            if need > days:  # Increase the capacity to ship within less days
                l = mid + 1
            else:  # Decrease the capacity to ship within more days
                r = mid
        return l
