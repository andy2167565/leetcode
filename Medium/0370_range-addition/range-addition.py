class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/range-addition/solutions/1339761/detailed-explanation-python/
        ans = [0] * length
        for start, end, inc in updates:
            ans[start] += inc
            if end + 1 < length:
                ans[end + 1] -= inc
        for i in range(1, length):
            ans[i] += ans[i - 1]
        return ans
