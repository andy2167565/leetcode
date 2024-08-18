class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Reference: https://leetcode.com/problems/earliest-possible-day-of-full-bloom/solutions/1676837/grow-then-plant/
        ans = 0
        for grow, plant in sorted(zip(growTime, plantTime)):
            ans = max(ans, grow) + plant
        return ans
