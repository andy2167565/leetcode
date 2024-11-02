class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i, j, n = 0, 1, len(nums)
        while i < n and j < n:
            if not nums[i] % 2:  # The even number is already in place
                i += 2
            elif nums[j] % 2:  # The odd number is already in place
                j += 2
            else:  # Both numbers are not in place
                nums[i], nums[j] = nums[j], nums[i]
        return nums
