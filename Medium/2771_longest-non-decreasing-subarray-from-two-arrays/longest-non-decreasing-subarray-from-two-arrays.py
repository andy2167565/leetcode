class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        ans = dp1 = dp2 = 1  # dp1: Maximum length ending with nums1[i]
        for i in range(1, len(nums1)):
            l11 = dp1 + 1 if nums1[i - 1] <= nums1[i] else 1
            l12 = dp1 + 1 if nums1[i - 1] <= nums2[i] else 1
            l21 = dp2 + 1 if nums2[i - 1] <= nums1[i] else 1
            l22 = dp2 + 1 if nums2[i - 1] <= nums2[i] else 1
            dp1 = max(l11, l21)
            dp2 = max(l12, l22)
            ans = max(ans, dp1, dp2)
        return ans
