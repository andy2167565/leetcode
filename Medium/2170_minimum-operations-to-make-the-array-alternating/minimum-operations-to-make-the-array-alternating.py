class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        import collections, itertools
        even, odd = [collections.Counter(nums[i::2]).most_common(2) + [(0, 0)] for i in range(2)]  # Pick the two most common elements from each list
        return len(nums) - max(a[1] + b[1] for a, b in itertools.product(even, odd) if a[0] != b[0])  # Secure different elements from each list that add up to the maximum frequency
