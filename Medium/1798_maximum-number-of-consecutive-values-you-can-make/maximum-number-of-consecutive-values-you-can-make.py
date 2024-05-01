class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        # Reference: https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/solutions/1118766/c-java-python-with-picture/
        ans = 1
        for val in sorted(coins):
            if val > ans:
                break
            ans += val
        return ans
