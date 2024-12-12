class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        import collections
        arr.sort()
        mad, diffs = float('inf'), collections.defaultdict(list)
        for i in range(len(arr) - 1):
            diff = arr[i + 1] - arr[i]
            diffs[diff].append([arr[i], arr[i + 1]])
            mad = min(mad, diff)
        return diffs[mad]
