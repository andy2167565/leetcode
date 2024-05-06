class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        import bisect
        absdiff = [abs(num1 - num2) for num1, num2 in zip(nums1, nums2)]
        ans, absdiffsum = float('inf'), sum(absdiff)
        nums1.sort()
        for num, diff in zip(nums2, absdiff):
            idx = bisect.bisect_left(nums1, num)
            if idx:
                ans = min(ans, absdiffsum - diff + abs(num - nums1[idx - 1]))
            if idx < len(nums1):
                ans = min(ans, absdiffsum - diff + abs(num - nums1[idx]))
        return ans % (10**9 + 7)
