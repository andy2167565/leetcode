class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/make-array-empty/solutions/3466800/java-c-python-easy-sort-solution/
        pos = {num: i for i, num in enumerate(nums)}
        ans = n = len(nums)  # Need at least len(nums) operations to remove all elements
        nums.sort()
        for i in range(1, n):
            if pos[nums[i - 1]] > pos[nums[i]]:  # Rotate sorted(nums)[i:] in original nums to the end so that the current minimum number sorted(nums)[i - 1] is moved to the beginning
                ans += n - i
        return ans
        # e.g. nums              = [4, 1, 5, 7, 2, 8, 9, 6, 3]
        #      Current iteration =           i
        #      sorted(nums)      = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #      Original position =  1  4  8  0  2  7  3  5  6
        # Number 4 to 9 are rotated to the end of nums behind 3
        # 1 and 2 are removed without rotation since they are smaller than 3
