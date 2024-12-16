class Solution:
    def dayOfYear(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split('-'))
        if not year % 400 or (not year % 4 and year % 100):
            days[1] += 1
        return sum(days[:month - 1]) + day
