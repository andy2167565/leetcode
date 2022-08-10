class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_num = 0
        while x > reversed_num:
            r = x % 10
            reversed_num = reversed_num * 10 + r 
            x //= 10

        return x == reversed_num or x == reversed_num//10
