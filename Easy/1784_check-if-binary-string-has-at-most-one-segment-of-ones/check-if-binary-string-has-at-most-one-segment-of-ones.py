class Solution:
    def checkOnesSegment(self, s: str) -> bool:
# My Post: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/discuss/2600403/Python-Groupby-One-liner-with-Explanation
#======== <Solution 1> ========#
        prev = 1
        for i in map(int, s[1:]):
            if not i:
                prev = i
            else:
                if not prev:
                    return False
        return True

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/discuss/1097891/Java-Simple-code-with-using-XOR
        switch, prev = 0, 1
        for i in map(int, s[1:]):
            if i ^ prev:
                switch += 1
                prev = i
                if switch > 1: return False
        return True

#======== <Solution 3> ========#
        import itertools
        return len(list(itertools.groupby(s))) < 3

#======== <Solution 4> ========#
        return '01' not in s

#======== <Solution 5> ========#
        return not s.strip('0').strip('1')

#======== <Solution 6> ========#
        # Reference: https://stackoverflow.com/questions/46044936/bitwise-and-between-negative-and-positive-numbers
        # First two lines will make num power of 2 if s contains only 1s or switches from 1 to 0 only once
        # e.g.                        111   1100   1001   10101
        num = int(s, 2)             #   7     12      9      21
        #(num & -num)                   1      4      1       1
        num += (num & -num)         #   8     16     10      22
        return not num & (num - 1)
