class Solution:
    def canPartition(self, nums: List[int]) -> bool:
#======== <Solution 1> ========#
        target, odd = divmod(sum(nums), 2)
        if odd: return False
        sums = {0}
        for num in nums:
            sums.update({(s + num) for s in sums})
        return target in sums

# Reference: https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624939/C%2B%2BPython-5-Simple-Solutions-w-Explanation-or-Optimization-from-Brute-Force-to-DP-to-Bitmask
#======== <Solution 2> ========#
        @cache
        def subsetSum(s, i):
            if not s: return True
            if i == len(nums) or s < 0: return False
            return subsetSum(s - nums[i], i + 1) or subsetSum(s, i + 1)
        target, odd = divmod(sum(nums), 2)
        return not odd and subsetSum(target, 0)

#======== <Solution 3> ========#
        target, odd = divmod(sum(nums), 2)
        if odd: return False
        dp = [True] + [False] * target  # dp[sum] denotes whether sum is achievable or not
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] |= dp[i - num]
        return dp[-1]

#======== <Solution 4> ========#
        target, odd = divmod(sum(nums), 2)
        if odd: return False
        dp = 1  # Each bit in bitset, i.e. dp[sum], denotes whether sum is possible or not
        for num in nums:
            dp |= dp << num
        return dp & 1 << target  # Return dp[target] denoting whether half sum is achievable or not
