class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#======== <Solution 1> ========#
        nums.sort()

#======== <Solution 2> ========#
        zeros = ones = twos = 0
        for num in nums:
            if not num:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        nums[:] = [0] * zeros + [1] * ones + [2] * twos

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
        # Assume all the elements to the left of white (nums[:white]) to be color-classified and all the elements to the right of (and including) white (nums[white:]) to be color-unclassified.
        # Swapping white with red leaves the element at white as color-classified, hence we can increment it. Swapping white with blue leaves the element at white as color-unclassified (as the element that white is now pointing at used to be pointed at by blue), hence we cannot increment it.
        red, white, blue = 0, 0, len(nums) - 1
        while white <= blue:
            if not nums[white]:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1

#======== <Solution 4> ========#
        # Reference: https://leetcode.com/problems/sort-colors/discuss/26479/AC-Python-in-place-one-pass-solution-O(n)-time-O(1)-space-no-swap-no-count
        red = white = 0
        for blue, num in enumerate(nums):
            nums[blue] = 2
            if num < 2:
                nums[white] = 1
                white += 1
            if not num:
                nums[red] = 0
                red += 1
