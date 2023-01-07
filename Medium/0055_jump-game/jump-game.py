class Solution:
    def canJump(self, nums: List[int]) -> bool:
#======== <Solution 1> ========#
        farthest = 0  # The maximum index we can reach so far
        for i, num in enumerate(nums):
            if i > farthest:  # We cannot go any further before nums ends
                return False
            farthest = max(farthest, i + num)
        return True

#======== <Solution 2> ========#
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:  # It is possible to reach goal from i
                goal = i
        return not goal
