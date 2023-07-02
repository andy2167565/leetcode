class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
#======== <Solution 1> ========#
        curr, zeros = n, 0
        while sum(map(int, str(curr))) > target:
            curr = curr // 10 + 1
            zeros += 1
        return curr * (10**zeros) - n

#======== <Solution 2> ========#
        x = zeros = 0
        while sum(map(int, str(n + x))) > target:
            zeros += 1
            x = 10**zeros - n % 10**zeros
        return x

#======== <Solution 3> ========#
        return 0 if sum(map(int, str(n))) <= target else 10 - (n % 10) + 10 * self.makeIntegerBeautiful(n // 10 + 1, target)
