class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        import math
        lo, hi = 1, 10**7 + 1
        while lo < hi:
            speed = lo + (hi - lo) // 2
            time = sum(math.ceil(dist[i] / speed) for i in range(len(dist) - 1)) + dist[-1] / speed
            if time > hour:
                lo = speed + 1
            else:
                hi = speed
        return -1 if lo == 10**7 + 1 else lo
