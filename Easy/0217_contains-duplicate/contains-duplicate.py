class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
#======== <Solution 1> ========#
        return len(set(nums)) != len(nums)

#======== <Solution 2> ========#
        nums.sort()
        return any(nums[i] == nums[i - 1] for i in range(1, len(nums)))

#======== <Solution 3> ========#
        import collections
        for count in collections.Counter(nums).values():
            if count > 1:
                return True
        return False

#======== <Solution 4> ========#
        single = {}
        for num in nums:
            if single.get(num, 0):
                return True
            single[num] = 1
        return False
