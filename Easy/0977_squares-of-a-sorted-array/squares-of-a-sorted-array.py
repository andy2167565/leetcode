class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        for i in range(len(nums)):
            nums[i] *= nums[i]
        nums.sort()
        return nums

#======== <Solution 2> ========#
        return sorted(num ** 2 for num in nums)

#======== <Solution 3> ========#
        l, r, ans = 0, len(nums) - 1, [0] * len(nums)
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                ans[r - l] = nums[r] ** 2
                r -= 1
            else:
                ans[r - l] = nums[l] ** 2
                l += 1
        return ans

#======== <Solution 4> ========#
        import collections
        l, r, ans = 0, len(nums) - 1, collections.deque()
        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                ans.appendleft(nums[r] ** 2)
                r -= 1
            else:
                ans.appendleft(nums[l] ** 2)
                l += 1
        return list(ans)
