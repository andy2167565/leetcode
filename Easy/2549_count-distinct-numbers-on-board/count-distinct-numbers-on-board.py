class Solution:
    def distinctIntegers(self, n: int) -> int:
#======== <Solution 1> ========#
        ans = 1
        while n > 2:
            for i in range(n - 1, 0, -1):
                if n % i == 1:
                    ans += 1
                    n = i
                    break
        return ans

#======== <Solution 2> ========#
        board = {n}
        while n > 1:
            for i in range(1, n):
                if n % i == 1:
                    board.add(i)
            n -= 1
        return len(board)

#======== <Solution 3> ========#
        return max(n - 1, 1)
