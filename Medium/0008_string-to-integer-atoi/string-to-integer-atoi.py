class Solution:
    def myAtoi(self, s: str) -> int:
#======== <Solution 1> ========#
        s = s.lstrip()
        sign = 1
        if s and s[0] in '+-':
            if s[0] == '-': sign = -1
            s = s[1:]
        num = 0
        for c in s:
            if not c.isdigit(): break
            num = 10 * num + int(c)
        return max(-2**31, min(2**31 - 1, sign * num))

#======== <Solution 2> ========#
        import re
        num = re.search(r"^[-+]?\d+", s.lstrip())
        return max(min(int(num.group(0)), 2**31-1), -2**31) if num else 0
