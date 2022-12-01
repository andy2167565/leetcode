class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Reference 1: https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
        # Reference 2: https://leetcode.com/problems/container-with-most-water/discuss/1069746/JS-Python-Java-C%2B%2B-or-2-Pointer-Solution-w-Visual-Explanation-or-beats-100
        l, r, ans = 0, len(height) - 1, 0
        while l < r:
            ans = max(ans, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
