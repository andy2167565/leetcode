class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # Reference: https://leetcode.com/problems/flip-string-to-monotone-increasing/solutions/184110/python-o-n-time-o-1-space-solution-with-explanation-with-extra-chinese-explanation/
        # Assume the string after flipping is s = '0' * i + '1' * j, where the index of first 1 is i
        # Flip all 1's before i to 0 and all 0's after i to 1
        # Iterate the string to find i that requires minimum number of flips
        min_flips = flips = s.count('0')  # Start from i = 0, i.e. flip all 0's to 1
        for c in s:  # Current index i refers to the next char of c in each round
            if c == '1':  # Flip c to 0
                flips += 1
            else:  # No need to flip c since it is already 0
                flips -= 1
                min_flips = min(min_flips, flips)
        return min_flips
