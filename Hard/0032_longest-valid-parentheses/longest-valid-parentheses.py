class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans, stack = 0, [-1]  # Store the index of each upper parenthesis we met
        for i, c in enumerate(s):
            if c == ')':
                stack.pop()
                if stack:  # There is valid upper parenthesis in stack
                    ans = max(ans, i - stack[-1])
                    continue
            stack.append(i)
        return ans
