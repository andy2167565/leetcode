class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-1/solutions/3446148/leetcode-the-hard-way-explained-line-by-line/
        n, ones = len(nums), nums.count(1)
        if ones:
            return n - ones
        min_ops = float('inf')
        for i in range(n):  # Find the shortest subarray with a gcd equal to 1
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_ops = min(min_ops, j - i)
        return -1 if min_ops == float('inf') else min_ops + n - 1  # The minimum operations to turn the shortest subarray to 1 + use that 1 to convert n - 1 elements to 1
