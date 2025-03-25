class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0
        for i, color in enumerate(colors):
            if color != colors[0]:
                ans = max(ans, i)
            if color != colors[-1]:
                ans = max(ans, len(colors) - 1 - i)
        return ans
