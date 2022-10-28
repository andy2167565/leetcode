class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#======== <Solution 1> ========#
        nums.sort(key=bool, reverse=True)

#======== <Solution 2> ========#
        # Reference 1: https://leetcode.com/problems/move-zeroes/discuss/562911/Two-pointers-technique-(Python-O(n)-time-O(1)-space)
        # Reference 2: https://leetcode.com/problems/move-zeroes/discuss/979820/Two-Pointeror-Visual-or-Python
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] and not nums[slow]:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow]:
                slow += 1
