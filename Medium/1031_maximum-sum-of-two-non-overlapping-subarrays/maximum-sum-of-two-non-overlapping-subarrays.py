class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
# Reference: https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/solutions/279221/java-python-3-two-easy-dp-codes-w-comment-time-o-n-no-change-of-input/
#======== <Solution 1> ========#
        def maxSum(l1, l2):
            max_l1 = max_total = 0
            for i in range(l1 + l2, len(prefixSum)):
                max_l1 = max(max_l1, prefixSum[i - l2] - prefixSum[i - l1 - l2])
                max_total = max(max_total, max_l1 + prefixSum[i] - prefixSum[i - l2])
            return max_total
        prefixSum = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            prefixSum[i + 1] = prefixSum[i] + num
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))

#======== <Solution 2> ========#
        def maxSum(l1, l2):
            sum_l1 = sum_l2 = 0
            for i in range(l1 + l2):
                if i < l1:
                    sum_l1 += nums[i]
                else:
                    sum_l2 += nums[i]
            max_l1, max_total = sum_l1, sum_l1 + sum_l2
            for i in range(l1 + l2, len(nums)):
                sum_l1 += nums[i - l2] - nums[i - l1 - l2]
                max_l1 = max(max_l1, sum_l1)
                sum_l2 += nums[i] - nums[i - l2]
                max_total = max(max_total, max_l1 + sum_l2)
            return max_total
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))

#======== <Solution 3> ========#
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        ans, max_l1, max_l2 = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
        for i in range(firstLen + secondLen, len(nums)):
            max_l1 = max(max_l1, nums[i - secondLen] - nums[i - firstLen - secondLen])  # Window: | --- L --- | --- M --- |
            max_l2 = max(max_l2, nums[i - firstLen] - nums[i - firstLen - secondLen])  # Window: | --- M --- | --- L --- |
            ans = max(ans, max_l1 + nums[i] - nums[i - secondLen], max_l2 + nums[i] - nums[i - firstLen])
        return ans
