class Solution:
    def trap(self, height: List[int]) -> int:
# Reference: https://leetcode.com/problems/trapping-rain-water/solutions/1374608/c-java-python-maxleft-maxright-so-far-with-picture-o-1-space-clean-concise/
#======== <Solution 1> ========#
        if len(height) < 3: return 0
        n = len(height)
        maxLeft, maxRight = [0] * n, [0] * n
        for i in range(1, n):  # Find maximum height at left-hand side for each bar
            maxLeft[i] = max(height[i - 1], maxLeft[i - 1])
        for i in range(n - 2, -1, -1):  # Find maximum height at right-hand side for each bar
            maxRight[i] = max(height[i + 1], maxRight[i + 1])
        ans = 0
        for i in range(1, n - 1):
            waterLevel = min(maxLeft[i], maxRight[i])
            if waterLevel > height[i]:
                ans += waterLevel - height[i]
        return ans

#======== <Solution 2> ========#
        if len(height) < 3: return 0
        n = len(height)
        maxLeft, maxRight = height[0], height[n - 1]
        left, right = 1, n - 2
        ans = 0
        while left <= right:
            if maxLeft < maxRight:
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1
        return ans
