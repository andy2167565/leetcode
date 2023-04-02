class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        return min(set(nums1) & set(nums2), default=0) or min(min(nums1), min(nums2)) * 10 + max(min(nums1), min(nums2))
