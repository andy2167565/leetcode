class Solution:
    def calculate(self, s: str) -> int:
        ans, num, prevSign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-':
                ans += prevSign * num
                num, prevSign = 0, [-1, 1][c == '+']
            elif c == '(':
                stack.extend([ans, prevSign])
                ans, prevSign = 0, 1
            elif c == ')':
                ans += prevSign * num
                ans *= stack.pop()  # Sign before current bracket
                ans += stack.pop()
                num = 0
        return ans + prevSign * num  # Need to add it back when last char is digit
