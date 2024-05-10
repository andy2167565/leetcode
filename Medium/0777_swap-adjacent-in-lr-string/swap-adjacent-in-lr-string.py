class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # Reference: https://leetcode.com/problems/swap-adjacent-in-lr-string/solutions/1536718/python-check-their-positions-with-picture-clean-concise/
        if start.replace('X', '') != end.replace('X', ''):  # The order of L's and R's must be the same
            return False
        startL, endL, startR, endR = [], [], [], []
        for i in range(len(start)):
            if start[i] == 'L':
                startL.append(i)
            if end[i] == 'L':
                endL.append(i)
            if start[i] == 'R':
                startR.append(i)
            if end[i] == 'R':
                endR.append(i)
        return all(i >= j for i, j in zip(startL, endL)) and all(i <= j for i, j in zip(startR, endR))
