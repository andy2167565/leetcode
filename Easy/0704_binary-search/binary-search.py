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

# Reference: https://leetcode.com/problems/binary-search/discuss/423162/Binary-Search-101
#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/binary-search/discuss/1914265/Binary-Search-for-beginners-(Intuition-building)
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

#======== <Solution 4> ========#
        # Reference: https://github.com/python/cpython/blob/3.10/Lib/bisect.py
        # A variation of bisect_left function in bisect module
        lo, hi = 0, len(nums) - 1  # hi = len(nums) - 1 since we won't insert target into nums. No need for a spare space to insert the number
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo if nums[lo] == target else -1

#======== <Solution 5> ========#
        import bisect
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
