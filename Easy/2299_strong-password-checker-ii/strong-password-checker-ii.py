class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        lower = upper = digit = special = False
        prev, special_char = '', '!@#$%^&*()-+'
        for c in password:
            if prev == c:
                return False
            lower = lower or c.islower()
            upper = upper or c.isupper()
            digit = digit or c.isdigit()
            special = special or c in special_char
            prev = c
        return lower and upper and digit and special
