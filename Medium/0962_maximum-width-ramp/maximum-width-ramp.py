class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
# Reference: https://leetcode.com/problems/maximum-width-ramp/solutions/208348/java-c-python-o-n-using-stack/
#======== <Solution 1> ========#
        import bisect
        ans, stack = 0, []  # Store the candidates for end point decreasingly by index
        for i in range(len(nums) - 1, -1, -1):
            if not stack or nums[i] > stack[-1][0]:  # Add nums[i] as candidate
                stack.append((nums[i], i))
            else:  # Find the point closest to the end of array
                j = stack[bisect.bisect(stack, (nums[i], i))][1]
                ans = max(ans, j - i)
        return ans

#======== <Solution 2> ========#
        ans, stack = 0, []  # Store the candidates for start point increasingly by index
        for i, num in enumerate(nums):
            if not stack or nums[stack[-1]] > num:  # Only need to add smaller numbers as candidates
                stack.append(i)
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                ans = max(ans, j - stack.pop())
        return ans
