class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
# Reference: https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/
#======== <Solution 1> ========#
        dp = [1] * len(nums)  # dp[i] is the longest increase subsequence of nums[:i+1]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

#======== <Solution 2> ========#
        import bisect
        sub = []
        for num in nums:
            if not sub or sub[-1] < num:
                sub.append(num)
            else:
                i = bisect.bisect_left(sub, num)  # Find the index of the first element >= num
                sub[i] = num  # Replace that number with num
        return len(sub)

#======== <Solution 3> ========#
        import bisect
        sub = []
        for num in nums:
            i = bisect.bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
        return len(sub)
