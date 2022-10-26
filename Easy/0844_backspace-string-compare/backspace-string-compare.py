class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
#======== <Solution 1> ========#
        def backspace(inString):
            outArray = []
            for c in inString:
                if c != '#':
                    outArray.append(c)
                elif outArray:
                    outArray.pop()
            return outArray
        return backspace(s) == backspace(t)

#======== <Solution 2> ========#
        def backspace(inString, outString='', back=0):
            for c in reversed(inString):
                if c == '#' or back:
                    back += 1 if c == '#' else -1
                else:
                    outString += c
            return outString
        return backspace(s) == backspace(t)

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/backspace-string-compare/discuss/135603/JavaC%2B%2BPython-O(N)-time-and-O(1)-space
        i, j = len(s) - 1, len(t) - 1
        backS = backT = 0
        while True:
            # i stops at non-deleted character in s or -1
            while i >= 0 and (backS or s[i] == '#'):
                backS += 1 if s[i] == '#' else -1
                i -= 1
            # j stops at non-deleted character in t or -1
            while j >= 0 and (backT or t[j] == '#'):
                backT += 1 if t[j] == '#' else -1
                j -= 1
            # Possible cases:
            # 1) (i == -1, j >= 0) or (i >= 0, j == -1): False  e.g. s = "a#", t = "a"
            # 2) i >= 0, j >= 0, s[i] != s[j]: False
            # 3) i == j == -1: True
            if i < 0 or j < 0 or s[i] != t[j]:
                return i == j == -1
            i, j = i - 1, j - 1
