class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        import collections, itertools
        hashmap, ans = collections.defaultdict(list), 0
        for i, prefix in enumerate(itertools.accumulate(nums, initial=0)):
            if prefix - target in hashmap:
                ans += 1
                hashmap.clear()
            hashmap[prefix] = i
        return ans
