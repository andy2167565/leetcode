class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0  # The end of the even part
        for i in range(len(nums)):
            if not nums[i] % 2:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
