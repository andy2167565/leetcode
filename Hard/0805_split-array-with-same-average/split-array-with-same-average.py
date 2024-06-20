class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        # Reference: https://leetcode.com/problems/split-array-with-same-average/solutions/120741/python-easy-and-concise-solution/
        memo = {}

        def find(target, k, i):  # Check if total k elements sums to target
            if not k:
                return not target
            if k + i > len(nums):
                return False
            if (target, k, i) in memo:
                return memo[(target, k, i)]
            memo[(target - nums[i], k - 1, i + 1)] = find(target - nums[i], k - 1, i + 1) or find(target, k, i + 1)
            return memo[(target - nums[i], k - 1, i + 1)]

        n, s = len(nums), sum(nums)
        return any(find(s * j // n, j, 0) for j in range(1, n // 2 + 1) if not s * j % n)
