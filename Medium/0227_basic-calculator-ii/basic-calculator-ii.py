class Solution:
    def calculate(self, s: str) -> int:
        stack, num, prevOp = [], 0, '+'  # Store previous operation before current num
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in '+-*/' or i == len(s) - 1:
                if prevOp == '+':
                    stack.append(num)
                elif prevOp == '-':
                    stack.append(-num)
                elif prevOp == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))  # Round down to the nearest whole number
                num, prevOp = 0, s[i]
        return sum(stack)
