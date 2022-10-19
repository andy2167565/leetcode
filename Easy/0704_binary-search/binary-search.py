class Solution:
    def search(self, nums: List[int], target: int) -> int:
#======== <Solution 1> ========#
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1

#======== <Solution 2> ========#
        if target in nums:
            return nums.index(target)
        return -1

#======== <Solution 3> ========#
        # Reference 1 :https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101
        # Reference 2: https://leetcode.com/problems/binary-search/discuss/1914265/Binary-Search-for-beginners-(Intuition-building)
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
