class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ans = prev = 0
        for p, s in sorted(zip(position, speed), reverse=True):  # Sort by position in reverse order
            t = (target - p) / s
            if t > prev:  # Current car is slower than the car ahead of it
                ans += 1
                prev = t
        return ans
