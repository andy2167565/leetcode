class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/contiguous-array/solutions/99655/python-o-n-solution-with-visual-explanation/
        ans, count, hashmap = 0, 0, {0: 0}  # Store the first index of every count as {count: index}
        for i, num in enumerate(nums, 1):
            count += num or -1
            if count in hashmap:  # A subarray with equal number of 0's and 1's starts and ends with the same count
                ans = max(ans, i - hashmap[count])
            else:  # Meet count for the first time
                hashmap[count] = i
        return ans
