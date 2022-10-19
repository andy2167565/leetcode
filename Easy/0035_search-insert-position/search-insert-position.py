class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
#======== <Solution 1> ========#
        for i, num in enumerate(nums):
            if num >= target:
                return i
        return len(nums)

#======== <Solution 2> ========#
        return sum(num < target for num in nums)

#======== <Solution 3> ========#
        if target not in nums:
            nums.append(target)
            nums.sort()
        return nums.index(target)

# Reference: https://leetcode.com/problems/search-insert-position/discuss/423166/Binary-Search-101
#======== <Solution 4> ========#
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) >> 1
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l

#======== <Solution 5> ========#
        # Reference: https://github.com/python/cpython/blob/3.10/Lib/bisect.py
        # bisect_left function in bisect module
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

#======== <Solution 6> ========#
        import bisect
        return bisect.bisect_left(nums, target)
