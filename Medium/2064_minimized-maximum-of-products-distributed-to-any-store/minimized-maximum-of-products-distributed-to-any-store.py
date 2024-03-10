class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/solutions/1563739/java-c-python-binary-search/
        l, r = 1, max(quantities)
        while l < r:
            mid = (l + r) // 2
            if sum((q + mid - 1) // mid for q in quantities) > n:
                l = mid + 1
            else:
                r = mid
        return l
