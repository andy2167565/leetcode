class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/solutions/768010/python-clean-greedy-solution-with-detailed-explanation-o-n-2/
        import itertools
        n, ans, trailing_zeros = len(grid), 0, [len(list(itertools.takewhile(lambda x: not x, row[::-1]))) for row in grid]
        for i in range(n):
            for j in range(i, n):
                trailing_zeros[i], trailing_zeros[j] = trailing_zeros[j], trailing_zeros[i]
                if trailing_zeros[i] >= n - i - 1:  # Bring row j to index i
                    ans += j - i
                    break
            else:
                return -1
        return ans
