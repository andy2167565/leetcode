class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
#======== <Solution 1> ========#
        return sorted(target) == sorted(arr)

#======== <Solution 2> ========#
        import collections
        return collections.Counter(target) == collections.Counter(arr)
