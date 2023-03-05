class Solution:
    def splitNum(self, num: int) -> int:
#======== <Solution 1> ========#
        num1, num2 = [], []
        for i, digit in enumerate(sorted(str(num))):
            (num1 if not i % 2 else num2).append(digit)
        return int(''.join(num1)) + int(''.join(num2))

#======== <Solution 2> ========#
        nums = ''.join(sorted(str(num)))
        return sum(map(int, (nums[::2], nums[1::2])))

#======== <Solution 3> ========#
        digits, ans = [], 0
        while num:
            num, digit = divmod(num, 10)
            digits.append(digit)
        if len(digits) % 2:
            digits.append(0)
        digits.sort()
        for i in range(0, len(digits), 2):
            ans = ans * 10 + digits[i] + digits[i + 1]
        return ans
