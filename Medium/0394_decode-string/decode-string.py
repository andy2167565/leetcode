class Solution:
    def decodeString(self, s: str) -> str:
        stack, curStr, curNum = [], '', 0
        for c in s:
            if c.isdigit():  # Parse k before next brackets
                curNum = curNum * 10 + int(c)
            elif c == '[':  # Start new brackets
                stack.append([curStr, curNum])  # Store parsed k and string right ahead of it
                curStr, curNum = '', 0  # Reset for contents inside new brackets
            elif c == ']':  # Current brackets end
                prevStr, num = stack.pop()  # Get latest k and string just ahead of current brackets
                curStr = prevStr + num * curStr  # Update current string with contents inside current brackets
            else:
                curStr += c
        return curStr
