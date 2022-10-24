class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        return [sum(nums[: i + 1]) for i in range(len(nums))]

#======== <Solution 2> ========#
        import itertools
        return list(itertools.accumulate(nums))

#======== <Solution 3> ========#
        result, total = [], 0
        for num in nums:
            total += num
            result.append(total)
        return result

#======== <Solution 4> ========#
        result = [nums[0]]
        for num in nums[1:]:
            result.append(result[-1] + num)
        return result

#======== <Solution 5> ========#
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
