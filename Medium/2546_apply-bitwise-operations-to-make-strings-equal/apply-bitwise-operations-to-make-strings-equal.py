class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
# Reference: https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/solutions/3083831/java-c-python-1-line-check-1/
#======== <Solution 1> ========#
        return ('1' in s) == ('1' in target)

#======== <Solution 2> ========#
        return max(s) == max(target)
