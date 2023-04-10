class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
# Reference: https://leetcode.com/problems/minimum-number-of-food-buckets-to-feed-the-hamsters/solutions/1598919/java-python-1-liner-solution/
#======== <Solution 1> ========#
        return -1 if 'HHH' in hamsters or 'HH' in (hamsters[:2], hamsters[-2:]) or hamsters == 'H' else hamsters.count('H') - hamsters.count('H.H')

#======== <Solution 2> ========#
        import re
        return -1 if re.search('(^|H)H(H|$)', hamsters) else hamsters.count('H') - hamsters.count('H.H')
