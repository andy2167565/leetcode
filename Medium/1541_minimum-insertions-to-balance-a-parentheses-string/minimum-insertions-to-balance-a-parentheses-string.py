class Solution:
    def minInsertions(self, s: str) -> int:
        # Reference: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/solutions/780199/java-c-python-straight-forward-one-pass/
        inserts = 0  # The number of left or right parentheses needed to be inserted to the string
        appends = 0  # The number of right parentheses needed to be appended to the string
        for c in s:
            if c == '(':
                if appends % 2:  # One of the right parentheses needs to be inserted into the middle of the string
                    appends -= 1
                    inserts += 1
                appends += 2
            else:
                appends -= 1
                if appends < 0:
                    appends += 2
                    inserts += 1  # Insert one left parenthesis for the invalid close
        return inserts + appends
