class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        nums.sort()
        return len({nums[i] + nums[~i] for i in range(len(nums) // 2)})

#======== <Solution 2> ========#
        import collections
        nums, seen = collections.deque(sorted(nums)), set()
        while nums:
            seen.add(nums.popleft() + nums.pop())
        return len(seen)
