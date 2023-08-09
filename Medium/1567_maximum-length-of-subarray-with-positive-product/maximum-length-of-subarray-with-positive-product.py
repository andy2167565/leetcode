class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = pos = neg = 0  # Length of subarrays with positive and negative products respectively
        for num in nums:
            if num > 0:  # +ve subarray remains +ve and -ve remains -ve after adding the new value
                pos, neg = pos + 1, neg + 1 if neg else 0
            elif num < 0:  # +ve subarray becomes -ve and -ve becomes +ve after adding the new value due to sign reversal
                pos, neg = neg + 1 if neg else 0, pos + 1  # Need to compute pos and neg at the same time with their original values
            else:  # Reset the subarrays
                pos = neg = 0
            ans = max(ans, pos)
        return ans
