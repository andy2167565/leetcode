class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Reference 1: https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/995249/python-increasing-stack-explained/
        # Reference 2: https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/28917/ac-python-clean-solution-using-stack-76ms/
        stack, ans = [], 0
        for i, height in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                ans = max(ans, h * w)
            stack.append(i)
        return ans
