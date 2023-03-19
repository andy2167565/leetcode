class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
# Reference: https://leetcode.com/problems/maximize-greatness-of-an-array/solutions/3312061/java-c-python-easy-and-concise-o-n/
#======== <Solution 1> ========#
        # Find the relationship between nums and perm
        nums.sort()
        ans = 0  # Current index
        for num in nums:
            if nums[ans] < num:  # num is the first number that is larger than nums[ans]
                ans += 1  # Put num in related_perm[ans] and move to next index
        return ans
        # e.g.    nums = [1, 3, 5, 2, 1, 3, 1]
        #  sorted_nums = [1, 1, 1, 2, 3, 3, 5]
        #          ans =              4
        # related_perm = [2, 3, 3, 5, 1, 1, 1]
        #         perm = [2, 1, 1, 5, 3, 1, 3]

#======== <Solution 2> ========#
        import collections
        return len(nums) - max(collections.Counter(nums).values())
