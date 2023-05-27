class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
#======== <Solution 1> ========#
        upper, lower = [], []
        for i, c in enumerate(s):
            if c == '(':
                upper.append(i)
            elif c == ')':
                if upper:
                    upper.pop()
                else:
                    lower.append(i)
        for i in sorted(upper + lower, reverse=True):
            s = s[:i] + s[i + 1:]
        return s

#======== <Solution 2> ========#
        s, stack = list(s), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        for i in stack:
            s[i] = ''
        return ''.join(s)
