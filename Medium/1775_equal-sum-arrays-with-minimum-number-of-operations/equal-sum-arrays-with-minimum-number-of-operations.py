class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # Reference: https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/solutions/1085786/java-python-3-2-greedy-codes-sort-and-count-w-brief-explanation-and-analysis/
        import collections
        if len(nums1) * 6 < len(nums2) or len(nums1) > len(nums2) * 6:
            return -1
        sum1, sum2 = map(sum, (nums1, nums2))
        if sum1 > sum2:  # Swap nums1 and nums2 if sum1 > sum2 to make sure sum1 <= sum2
            return self.minOperations(nums2, nums1)
        count = collections.Counter([6 - num for num in nums1] + [num - 1 for num in nums2])  # Count the increases in nums1 and decreases in nums2
        i, operations = 5, 0
        while sum2 > sum1:
            while not count[i]:
                i -= 1
            sum1 += i
            count[i] -= 1
            operations += 1
        return operations
