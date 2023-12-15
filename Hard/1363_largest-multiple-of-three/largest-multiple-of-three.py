class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
#======== <Solution 1> ========#
        import collections
        total, freqs = sum(digits), collections.Counter(digits)
        digits.sort(reverse=True)

        def removeDigit(i):
            if freqs[i]:
                digits.remove(i)
                freqs[i] -= 1
            if not digits:  # No digit left
                return ''
            if not any(digits):  # All digits are 0
                return '0'
            if not sum(digits) % 3:  # Use all existing digits
                return ''.join(map(str, digits))

        if not total % 3:  # Use all digits
            return removeDigit(-1)
        if total % 3 == 1:
            if freqs[1] + freqs[4] + freqs[7]:  # Remove one digit in (1, 4, 7)
                return removeDigit(1) or removeDigit(4) or removeDigit(7)
            return removeDigit(2) or removeDigit(2) or removeDigit(5) or removeDigit(5) or removeDigit(8) or removeDigit(8)  # Remove two identical digits in (2, 5, 8)
        if total % 3 == 2:
            if freqs[2] + freqs[5] + freqs[8]:  # Remove one digit in (2, 5, 8)
                return removeDigit(2) or removeDigit(5) or removeDigit(8)
            return removeDigit(1) or removeDigit(1) or removeDigit(4) or removeDigit(4) or removeDigit(7) or removeDigit(7)  # Remove two identical digits in (1, 4, 7)

#======== <Solution 2> ========#
        import sys
        sys.set_int_max_str_digits(0)
        dp = [-1] * 3  # dp[i]: The largest number with remainder equal to i
        for d in sorted(digits, reverse=True):
            for curr in dp + [0]:
                num = curr * 10 + d
                dp[num % 3] = max(dp[num % 3], num)
        return str(dp[0]) if dp[0] >= 0 else ''
