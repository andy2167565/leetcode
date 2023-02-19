class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimum-score-by-changing-two-elements/solutions/3202036/python-2-line-solution-w-explanation/
        nums.sort()
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])
