class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        unique_index = 0
        for value in nums:
            if nums[unique_index] != value:
                unique_index += 1
                nums[unique_index] = value
        
        return unique_index + 1
