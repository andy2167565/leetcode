class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
#======== <Solution 1> ========#
        ans = 0
        if len(nums2) % 2:
            for num in nums1:
                ans ^= num
        if len(nums1) % 2:
            for num in nums2:
                ans ^= num
        return ans

#======== <Solution 2> ========#
        import functools, operator
        return functools.reduce(operator.xor, nums1 * (len(nums2) & 1) + nums2 * (len(nums1) & 1), 0)
