from itertools import combinations

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for (i, j) in combinations(range(len(nums)), 2):
            if nums[i] + nums[j] == target:
                return [i, j]
