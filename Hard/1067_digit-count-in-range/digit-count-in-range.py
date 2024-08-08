class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        # Reference: https://leetcode.com/problems/digit-count-in-range/solutions/609476/python-solution-with-explanation/
        def getCounts(num):
            count, suffix, weight = 0, 0, 1
            while num:
                num, digit = divmod(num, 10)
                if digit > d:
                    count += (num + 1 - (d == 0)) * weight
                elif digit == d:
                    count += (num - (d == 0)) * weight + suffix + 1
                else:
                    count += (num - (d == 0)) * weight
                suffix += digit * weight
                weight *= 10
            return count

        return getCounts(high) - getCounts(low - 1)
