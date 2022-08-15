class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
#======== <Solution 1> ========#
        count = 1
        while '0' in str(count) + str(n - count):
            count += 1
        return [count, n - count]

#======== <Solution 2> ========#
        for i in range(1, n):
            if '0' not in str(i) + str(n - i):
                return [i, n - i]
