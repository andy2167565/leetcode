class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution
        pigs = 0
        while (minutesToTest // minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs

#======== <Solution 2> ========#
        import math
        return math.ceil(math.log2(buckets) / math.log2(minutesToTest // minutesToDie + 1))
