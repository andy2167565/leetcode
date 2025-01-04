class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        return int(''.join(map(min, *map('{:04}'.format, [num1, num2, num3]))))
