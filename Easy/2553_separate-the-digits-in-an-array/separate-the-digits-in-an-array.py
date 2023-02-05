class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        ans = []
        for num in nums[::-1]:
            while num:
                num, digit = divmod(num, 10)
                ans.append(digit)
        return ans[::-1]

#======== <Solution 2> ========#
        return [int(digit) for num in nums for digit in str(num)]
