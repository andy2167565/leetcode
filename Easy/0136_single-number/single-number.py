class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        single = set()
        for num in nums:
            if num in single:
                single.remove(num)
            else:
                single.add(num)
        return single.pop()

#======== <Solution 2> ========#
        import collections
        return collections.Counter(nums).most_common()[-1][0]

#======== <Solution 3> ========#
        import itertools
        return next(g[0] for g in itertools.groupby(sorted(nums)) if len(list(g[1])) == 1)

#======== <Solution 4> ========#
        nums.sort()
        pair = False
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] and not pair:
                return nums[i - 1]
            else:
                pair = nums[i] == nums[i - 1]
        return nums[-1]

#======== <Solution 5> ========#
        return 2 * sum(set(nums)) - sum(nums)

#======== <Solution 6> ========#
        xor = 0
        for num in nums:
            xor ^= num
        return xor

#======== <Solution 7> ========#
        while len(nums) > 1:
            nums[0] ^= nums.pop()
        return nums.pop()

#======== <Solution 8> ========#
        import functools, operator
        return functools.reduce(operator.xor, nums)
