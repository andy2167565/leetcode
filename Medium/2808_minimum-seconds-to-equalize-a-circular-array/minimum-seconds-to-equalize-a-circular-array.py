class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/solutions/3867958/java-python-3-min-of-the-longest-distance-between-same-numbers/
        import collections, itertools
        nums += nums  # Make nums a circular array
        indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            indices[num].append(i)
        return min(max(j - i for i, j in itertools.pairwise(arr)) // 2 for arr in indices.values())
