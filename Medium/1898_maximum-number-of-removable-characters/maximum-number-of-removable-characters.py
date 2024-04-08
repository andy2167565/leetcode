class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def isSubseq(x):
            """Return True if p is a subsequence of s after x removals."""
            k = 0
            for i, c in enumerate(s):
                if removed.get(i, float('inf')) >= x and k < len(p) and c == p[k]:
                    k += 1
            return k == len(p)
        
        removed, lo, hi = {i: pos for pos, i in enumerate(removable)}, -1, len(removable)
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if isSubseq(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo
