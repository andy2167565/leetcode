class Solution:
    def baseNeg2(self, n: int) -> str:
# Reference: https://leetcode.com/problems/convert-to-base-2/solutions/265507/java-c-python-2-lines-exactly-same-as-base-2/
#======== <Solution 1> ========#
        ans = []
        while n:
            ans.append(n & 1)
            n = -(n >> 1)
        return ''.join(map(str, ans[::-1] or [0]))

#======== <Solution 2> ========#
        return str(n) if n in (0, 1) else self.baseNeg2(-(n >> 1)) + str(n & 1)
