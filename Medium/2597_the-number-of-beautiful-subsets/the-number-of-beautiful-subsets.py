class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/the-number-of-beautiful-subsets/solutions/3314361/python-house-robber-o-n/
        import collections, functools, operator
        counter = collections.Counter(nums)

        def dp(num):  # dp(num): The result for sequence no bigger than num
            dp0, dp1 = dp(num - k) if num - k in counter else (1, 0)
            return dp0 + dp1, dp0 * (pow(2, counter[num]) - 1)  # (The ways without num, The ways with num)

        return functools.reduce(operator.mul, (sum(dp(num)) for num in counter if not counter[num + k])) - 1
