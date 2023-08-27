class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
#======== <Solution 1> ========#
        ans = imax = 0
        for i, val in enumerate(values):  # For any index j, the score is maximized by the best value of values[i] + i seen before since values[j] - j is fixed
            ans = max(ans, imax + val - i)  # values[i] + i + values[j] - j
            imax = max(imax, val + i)  # The maximum values[i] + i in next round
        return ans

#======== <Solution 2> ========#
        ans = prev_max = 0
        for val in values:
            ans = max(ans, prev_max + val)  # values[i] + i - j + values[j]
            prev_max = max(prev_max, val) - 1  # values[i] + i - j
        return ans
