class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
# Reference: https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/1229403/JS-Python-Java-C%2B%2B-or-Easy-Stack-Solution-w-Explanation
#======== <Solution 1> ========#
        import operator
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        stack = []
        for c in tokens:
            if c in operators:
                r, l = stack.pop(), stack.pop()
                stack.append(int(operators[c](l, r)))
            else:
                stack.append(int(c))
        return stack.pop()

#======== <Solution 2> ========#
        operators = {
            '+': lambda b, a: a + b,
            '-': lambda b, a: a - b,
            '*': lambda b, a: a * b,
            '/': lambda b, a: int(a / b)
        }
        stack = []
        for c in tokens:
            if c in operators:
                stack.append(operators[c](stack.pop(), stack.pop()))
            else:
                stack.append(int(c))
        return stack.pop()

#======== <Solution 3> ========#
        stack = []
        for c in tokens:
            if c in '+-*/':
                r, l = stack.pop(), stack.pop()
                stack.append(str(int(eval(l + c + r))))
            else:
                stack.append(c)
        return int(stack.pop())
