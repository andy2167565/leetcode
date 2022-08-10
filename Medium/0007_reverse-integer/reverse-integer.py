class Solution:
    def reverse(self, x: int) -> int:
#======== <Solution 1> ========#
        reversed_num = int(''.join(reversed(list(str(abs(x))))))
        reversed_num = -reversed_num if x < 0 else reversed_num
        return reversed_num if -pow(2, 31) <= reversed_num <= pow(2, 31)-1 else 0

#======== <Solution 2> ========#
        if x < 0:
            return -self.reverse(-x)
        elif x == 0:
            return 0
        else:
            ans = 0
            while x > 0:
                x, r = divmod(x, 10)
                ans = 10 * ans + r
            return ans if ans <= 2**31 - 1 else 0
