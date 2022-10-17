class Solution:
    def sum(self, num1: int, num2: int) -> int:
# Reference: https://leetcode.com/problems/add-two-integers/discuss/1968134/21-different-ways-to-solve-this-problem
#======== <Solution 1> ========#
        return num1 + num2

#======== <Solution 2> ========#
        l, r = -200, 200
        while l < r:
            mid = (l + r) >> 1  # (l + r) // 2
            if mid == num1 + num2: return mid
            if mid < num1 + num2: l = mid + 1
            if mid > num1 + num2: r = mid - 1
        return l  # l == r

#======== <Solution 3> ========#
        for i in range(-200, 201):
            if num1 + num2 == i:
                return i

#======== <Solution 4> ========#
        ans = 0
        sign = lambda num: (num > 0) * 2 - 1
        while num1:
            ans += sign(num1)
            num1 -= sign(num1)
        while num2:
            ans += sign(num2)
            num2 -= sign(num2)
        return ans

# Reference: https://leetcode.com/problems/add-two-integers/discuss/2023595/JavaPython-3-Bit-manipulations-wo-using-%2B-or-Iterative-and-recursive-codes.
#======== <Solution 5> ========#
        # num1 stores output, num2 stores carry over
        mask = 0xFFFF
        while num2 & mask:
            num1, num2 = num1 ^ num2, (num1 & num2) << 1  # sum without carry over vs. carry over
        return num1 if num2 < mask else num1 & mask

#======== <Solution 6> ========#
        mask = 0xFFFF
        if not num2 & mask:
            return num1 if num2 < mask else num1 & mask
        return self.sum(num1 ^ num2, (num1 & num2) << 1)
