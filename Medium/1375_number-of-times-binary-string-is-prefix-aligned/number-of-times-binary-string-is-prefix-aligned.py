class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
# Reference: https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/discuss/532538/JavaC%2B%2BPython-Straight-Forward-O(1)-Space
#======== <Solution 1> ========#
        count = M = 0
        for i, num in enumerate(flips, 1):
            M = max(M, num)
            count += M == i
        return count

#======== <Solution 2> ========#
        import itertools, operator
        return sum(map(operator.eq, itertools.accumulate(flips, max), itertools.count(1)))

#======== <Solution 3> ========#
        import itertools
        return sum(i == num for i, num in enumerate(itertools.accumulate(flips, max), 1))
