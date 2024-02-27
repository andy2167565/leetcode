class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Reference: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/solutions/203182/java-c-python-greedy-solution-o-mn/
        ans, n, l = 0, len(strs), len(strs[0])
        is_sorted = [0] * (n - 1)
        for j in range(l):
            is_sorted2 = is_sorted[:]
            for i in range(n - 1):
                if strs[i][j] > strs[i + 1][j] and not is_sorted[i]:
                    ans += 1
                    break
                is_sorted2[i] |= strs[i][j] < strs[i + 1][j]
            else:
                is_sorted = is_sorted2
        return ans
