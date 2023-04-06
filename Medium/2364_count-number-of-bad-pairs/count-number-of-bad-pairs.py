class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # Reference: https://leetcode.com/problems/count-number-of-bad-pairs/solutions/2388121/python-o-n-solution-how-to-reverse-a-problem-to-make-it-easier-to-solve/
        import collections
        good, diff_map = 0, collections.defaultdict(int)
        for i, num in enumerate(nums):
            good += diff_map[i - num]
            diff_map[i - num] += 1
        return len(nums) * (len(nums) - 1) // 2 - good
