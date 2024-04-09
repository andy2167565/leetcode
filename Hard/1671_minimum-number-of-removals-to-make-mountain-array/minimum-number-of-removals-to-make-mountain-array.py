class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/solutions/952053/python-3-solutions-lis-dp-o-n-log-n-explained/
        n = len(nums)
        lis = [1] * n  # lis[i]: Maximum length of longest increasing subsequence ending with index i
        ma = [1] * n  # ma[i]: Maximum length of mountain array ending with index i
        for j in range(1, n):
            for i in range(j):
                if nums[i] < nums[j]:
                    lis[j] = max(lis[j], lis[i] + 1)
                if nums[i] > nums[j]:
                    if lis[i] > 1:
                        ma[j] = max(ma[j], lis[i] + 1)
                    if ma[i] > 1:
                        ma[j] = max(ma[j], ma[i] + 1)
        return n - max(ma)
