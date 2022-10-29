class Solution:
    def isPalindrome(self, x: int) -> bool:
#======== <Solution 1> ========#
        return str(x) == str(x)[::-1]

#======== <Solution 2> ========#
        if x < 0 or (x and not x % 10): return False
        if x < 10: return True
        reversed_num = 0
        # Reverse the last half of the integer
        while x > reversed_num:
            x, r = divmod(x, 10)
            reversed_num = reversed_num * 10 + r
        return x == reversed_num or x == reversed_num // 10  # Even length or odd length integer
