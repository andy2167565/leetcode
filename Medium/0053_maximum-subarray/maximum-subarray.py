class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        result = nums[0]
        current_sum = 0
        for num in nums:
            # Remove negative prefix sum
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            result = max(result, current_sum)
        return result
        
#======== <Solution 2> ========#
        result = nums[0]
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            result = max(result, current_sum)
        return result
