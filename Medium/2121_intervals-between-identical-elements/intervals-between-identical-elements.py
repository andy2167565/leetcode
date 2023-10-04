class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/intervals-between-identical-elements/solutions/1647630/python3-java-c-dictionary-map-and-prefix-sum-o-n/
        import collections, itertools
        location, intervals = collections.defaultdict(list), [0] * len(arr)
        for i, num in enumerate(arr):
            location[num].append(i)
        for idx_list in location.values():
            prefix = list(itertools.accumulate(idx_list, initial=0))
            for i, idx in enumerate(idx_list):
                l = idx * i - prefix[i]  # Sum of differences for indexes smaller than or equal to i
                r = (prefix[-1] - prefix[i]) - idx * (len(idx_list) - i)  # Sum of differences for indexes larger than i
                intervals[idx] = l + r
        return intervals
