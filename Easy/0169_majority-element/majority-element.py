class Solution:
    def majorityElement(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        for num in set(nums):
            if nums.count(num) > len(nums) // 2:
                return num

#======== <Solution 2> ========#
        return next(num for num in set(nums) if nums.count(num) > len(nums) // 2)

#======== <Solution 3> ========#
        return sorted(nums)[len(nums) // 2]

#======== <Solution 4> ========#
        majority, count = None, 0
        for num in nums:
            if not count: majority = num
            count += 1 if num == majority else -1
        return majority
