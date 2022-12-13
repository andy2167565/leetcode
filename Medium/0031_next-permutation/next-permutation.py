class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/next-permutation/solutions/13907/easy-python-solution-based-on-lexicographical-permutation-algorithm/
        i = successor = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:  # Find longest non-increasing suffix
            i -= 1
        if not i:  # nums are in non-increasing order
            nums.reverse()
            return
        pivot = i - 1  # Get the index before the last peak
        while nums[pivot] >= nums[successor]:  # Find rightmost successor to pivot in the suffix
            successor -= 1
        nums[pivot], nums[successor] = nums[successor], nums[pivot]
        l, r = pivot + 1, len(nums) - 1  # Reverse the suffix
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/next-permutation/solutions/1909728/simple-9-line-python-solution-with-detailed-explanation-easy-understand-for-beginners/
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:  # Find the index of the last peak
                nums[i:] = sorted(nums[i:])  # Reverse the suffix
                pivot = i - 1  # Get the index before the last peak
                for successor in range(i, len(nums)):  # Find rightmost successor to pivot in the suffix and swap them
                    if nums[pivot] < nums[successor]:
                        nums[pivot], nums[successor] = nums[successor], nums[pivot]
                        return
        nums.reverse()
