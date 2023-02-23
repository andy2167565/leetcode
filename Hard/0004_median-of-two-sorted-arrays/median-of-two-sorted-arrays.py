class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#======== <Solution 1> ========#
        nums = sorted(nums1 + nums2)
        return (nums[len(nums) // 2] + nums[(len(nums) - 1) // 2]) / 2

#======== <Solution 2> ========#
        l = len(nums1) + len(nums2)
        return self.kth(nums1, nums2, l // 2) if l % 2 else (self.kth(nums1, nums2, l // 2) + self.kth(nums1, nums2, l // 2 - 1)) / 2

    def kth(self, a, b, k):
        if len(a) > len(b): a, b = b, a
        if not a: return b[k]
        if k == len(a) + len(b) - 1: return max(a[-1], b[-1])
        i = len(a) // 2
        j = k - i
        return self.kth(a[:i], b[j:], i) if a[i] > b[j] else self.kth(a[i:], b[:j], j)

#======== <Solution 3> ========#
        import bisect
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) // 2
        i = bisect.bisect_left(range(m), True, key=lambda i: after - i - 1 < 0 or a[i] >= b[after - i - 1])
        nextfew = sorted(a[i: i + 2] + b[after - i: after - i + 2])
        return (nextfew[0] + nextfew[1 - (m + n) % 2]) / 2
