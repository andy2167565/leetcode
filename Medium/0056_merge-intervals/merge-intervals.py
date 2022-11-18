class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Reference: https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python
        ans = []
        for i in sorted(intervals, key=lambda x: x[0]):
            if ans and i[0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], i[1])
            else:
                ans.append(i)
        return ans
