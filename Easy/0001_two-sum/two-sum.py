class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
#======== <Solution 1> ========#
        from itertools import combinations
        for (i, j) in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]
        
#======== <Solution 2> ========#
        while nums:
            num = nums.pop()
            if target - num in nums:
                return [nums.index(target - num), len(nums)]
