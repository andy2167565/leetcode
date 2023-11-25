class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
#======== <Solution 1> ========#
        import collections
        dp = collections.defaultdict(int)  # dp[i, j]: The maximum number of uncrossed lines between the first i + 1 elements of nums1 and the first j + 1 elements of nums2
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i, j] = max(dp[i - 1, j - 1] + (nums1[i] == nums2[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[len(nums1) - 1, len(nums2) - 1]

#======== <Solution 2> ========#
        dp = [0] * (len(nums2) + 1)  # dp[i]: The maximum number of uncrossed lines between the first i elements of nums1 and all elements of nums2
        for i in range(1, len(nums1) + 1):
            prev = 0
            for j in range(1, len(nums2) + 1):
                curr = dp[j]
                dp[j] = max(dp[j - 1], curr, prev + (nums1[i - 1] == nums2[j - 1]))
                prev = curr
        return dp[-1]
