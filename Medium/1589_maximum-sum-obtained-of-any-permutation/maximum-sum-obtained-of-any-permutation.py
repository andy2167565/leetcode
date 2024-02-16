class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/solutions/854206/java-c-python-sweep-line/
        import itertools
        counter = [0] * (len(nums) + 1)
        for start, end in requests:
            counter[start] += 1
            counter[end + 1] -= 1
        return sum(count * num for count, num in zip(sorted(list(itertools.accumulate(counter))[:-1]), sorted(nums))) % (10**9 + 7)
