class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        import itertools
        return [g[0] for g in itertools.groupby(sorted(nums)) if len(list(g[1])) == 2]

#======== <Solution 2> ========#
        temp, ans = 0, []
        for i, j in zip(list(range(1, len(nums) + 1)), sorted(nums)):
            if i - j == temp + 1:
                ans.append(j)
            temp = i - j
        return ans

# Reference: https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/775738/Python-2-solutions-with-O(n)-timeO(1)-space-explained
#======== <Solution 3> ========#
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [nums[i] for i in range(len(nums)) if i != nums[i] - 1]

#======== <Solution 4> ========#
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return ans
