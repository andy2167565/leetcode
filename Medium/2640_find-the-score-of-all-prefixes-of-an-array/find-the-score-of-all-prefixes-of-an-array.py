class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        ans, M = [], 0
        for num in nums:
            M = max(M, num)
            ans.append(num + M + (ans[-1] if ans else 0))
        return ans

#======== <Solution 2> ========#
        import itertools
        conver, M = [], 0
        for num in nums:
            M = max(M, num)
            conver.append(num + M)
        return itertools.accumulate(conver)

#======== <Solution 3> ========#
        import itertools
        return itertools.accumulate(num + M for num, M in zip(nums, itertools.accumulate(nums, max)))
