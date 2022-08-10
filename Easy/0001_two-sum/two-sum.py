class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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

#======== <Solution 3> ========#
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i
