class Solution:
    def findMin(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        return min(nums)

#======== <Solution 2> ========#
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]

#======== <Solution 3> ========#
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
