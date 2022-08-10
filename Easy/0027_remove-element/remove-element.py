class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
#======== <Two Pointers Solution> ========#
        if len(nums) == 0:
            return 0
        
        remain_index = 0
        for value in nums:
            if value != val:
                nums[remain_index] = value
                remain_index += 1
        
        return remain_index
        
#======== <Two Pointers with Rare Elements Solution> ========#
        if len(nums) == 0:
            return 0
        
        current_index = 0
        remain_index = len(nums)
        while current_index < remain_index:
            if nums[current_index] == val:
                nums[current_index] = nums[remain_index-1]
                remain_index -= 1
            else:
                current_index += 1
        
        return remain_index
