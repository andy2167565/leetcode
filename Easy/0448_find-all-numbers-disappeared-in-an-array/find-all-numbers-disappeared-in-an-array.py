class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        return list(set(range(1, len(nums) + 1)) - set(nums))

#======== <Solution 2> ========#
        seen = [False] * len(nums)
        for num in nums:
            seen[num - 1] = True
        return [i + 1 for i in range(len(nums)) if not seen[i]]

#======== <Solution 3> ========#
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]
