class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        import collections
        nums, ans = collections.deque(nums), 0
        while nums:
            l = str(nums.popleft())
            r = str(nums.pop()) if nums else ''
            ans += int(l + r)
        return ans

#======== <Solution 2> ========#
        mid, r = divmod(len(nums), 2)
        ans = nums[mid] if r else 0
        for i in range(mid):
            ans += int(str(nums[i]) + str(nums[~i]))
        return ans
