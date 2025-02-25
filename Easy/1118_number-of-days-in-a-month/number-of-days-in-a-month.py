class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days[month - 1] + (month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0))
