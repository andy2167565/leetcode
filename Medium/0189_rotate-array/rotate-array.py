class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#======== <Solution 1> ========#
        nums[:] = nums[-k % len(nums):] + nums[:-k % len(nums)]

#======== <Solution 2> ========#
        for _ in range(k):
            nums.insert(0, nums.pop())

#======== <Solution 3> ========#
        from collections import deque
        d = deque(nums)
        d.rotate(k)
        nums[:] = list(d)

# Reference: https://leetcode.com/problems/rotate-array/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
#======== <Solution 4> ========#
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[(i + k) % len(nums)] = nums[i]
        nums[:] = ans

#======== <Solution 5> ========#
        count = start = 0
        while count < len(nums):
            current = start
            prev = nums[start]
            while True:
                current = (current + k) % len(nums)
                nums[current], prev = prev, nums[current]
                count += 1
                if current == start:
                    break
            start += 1

#======== <Solution 6> ========#
        def reverse(arr: List[int], left: int, right: int) -> None:
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        k %= len(nums)
        if k:
            reverse(nums, 0, len(nums) - 1)
            reverse(nums, 0, k - 1)
            reverse(nums, k, len(nums) - 1)
