class Solution:
    def search(self, nums: List[int], target: int) -> int:
#======== <Solution 1> ========#
        return nums.index(target) if target in nums else -1

# Reference: https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
#======== <Solution 2> ========#
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[0] <= nums[mid]:  # nums[mid] is on the left side
                if nums[0] <= target:  # target is on the left side
                    if nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid
                else:  # target is on the right side
                    l = mid + 1
            else:  # nums[mid] is on the right side
                if target < nums[0]:  # target is on the right side
                    if nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid
                else:  # target is on the left side
                    r = mid
        return l if nums[l] == target else -1

#======== <Solution 3> ========#
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            # nums[mid] is on the left side and target is on the right side
            if target < nums[0] <= nums[mid]:
                l = mid + 1
            # target is on the left side and nums[mid] is on the right side
            elif nums[mid] < nums[0] <= target:
                r = mid
            # Both nums[mid] and target are on the same side
            elif nums[mid] < target:
                l = mid + 1
            elif target < nums[mid]:
                r = mid
            # nums[mid] == target
            else:
                return mid
        return -1

#======== <Solution 4> ========#
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if (nums[mid] < nums[0]) == (target < nums[0]):  # Both nums[mid] and target are on the same side
                num = nums[mid]
            elif target < nums[0]:  # nums[mid] is on the left side and target is on the right side
                num = float('-inf')
            else:  # target is on the left side and nums[mid] is on the right side
                num = float('inf')

            if num < target:
                l = mid + 1
            elif target < num:
                r = mid
            else:
                return mid
        return -1
