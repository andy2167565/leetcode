class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/make-k-subarray-sums-equal/solutions/3366442/python3-find-median-of-each-gcd-defined-subarray-w-examples/
        import math
        ans, g = 0, math.gcd(len(arr), k)
        for i in range(g):
            nums = sorted(arr[j] for j in range(i, len(arr), g))
            median = nums[len(nums) // 2]
            ans += sum(abs(num - median) for num in nums)
        return ans
