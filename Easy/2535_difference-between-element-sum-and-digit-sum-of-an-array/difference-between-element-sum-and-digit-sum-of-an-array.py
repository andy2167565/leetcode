class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        digit_sum = 0
        for num in nums:
            while num:
                num, digit = divmod(num, 10)
                digit_sum += digit
        return abs(sum(nums) - digit_sum)

#======== <Solution 2> ========#
        return sum(num - sum(map(int, str(num))) for num in nums)
