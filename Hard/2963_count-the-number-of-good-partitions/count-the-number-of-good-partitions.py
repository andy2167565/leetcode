class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/count-the-number-of-good-partitions/solutions/4384415/java-c-python-two-passes/
        ans, j, last = 1, 0, {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            if i > j:  # Either continue the current subarray or start a new one
                ans = ans * 2 % (10**9 + 7)
            j = max(j, last[num])  # The index of last occurrence of num
        return ans
