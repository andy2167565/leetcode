# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
#======== <Solution 1> ========#
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        return l

#======== <Solution 2> ========#
        import bisect
        return bisect.bisect_left(range(n), True, 1, key=isBadVersion)
