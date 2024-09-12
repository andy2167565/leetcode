class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        ans = 0
        for i, h1 in enumerate(hours):
            for j, h2 in enumerate(hours[i + 1:], i + 1):
                ans += not (h1 + h2) % 24
        return ans
