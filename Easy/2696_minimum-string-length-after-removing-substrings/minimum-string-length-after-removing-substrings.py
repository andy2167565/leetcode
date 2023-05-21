class Solution:
    def minLength(self, s: str) -> int:
#======== <Solution 1> ========#
        while 'AB' in s or 'CD' in s:
            s = s.replace('AB', '').replace('CD', '')
        return len(s)

#======== <Solution 2> ========#
        stack = []
        for c in s:
            if stack and stack[-1] + c in ('AB', 'CD'):
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
