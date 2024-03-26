class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/solutions/3341928/c-java-python3-prefix-sums-binary-search/
        import itertools, bisect
        nums.sort()
        prefix = list(itertools.accumulate(nums, initial=0))
        splits = [(q, bisect.bisect_left(nums, q)) for q in queries]
        return [q * (2 * i - len(nums)) + prefix[-1] - 2 * prefix[i] for q, i in splits]
