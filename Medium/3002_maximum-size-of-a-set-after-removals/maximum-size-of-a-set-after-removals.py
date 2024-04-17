class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
#======== <Solution 1> ========#
        n, s1, s2 = len(nums1), set(nums1), set(nums2)
        inner = s1.intersection(s2)
        remain1 = min(len(s1) - len(inner), n // 2)
        remain2 = min(len(s2) - len(inner), n // 2)
        return min(remain1 + remain2 + len(inner), n)

#======== <Solution 2> ========#
        n, s1, s2 = len(nums1), set(nums1), set(nums2)
        n1, n2, n3 = len(s1), len(s2), len(s1 & s2)
        return min(n1 + n2 - n3, min(n1, n // 2) + min(n2, n // 2))
