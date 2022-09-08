class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
#======== <Solution 1> ========#
        if not nums: return []
        nums.append(float('inf'))
        ans, start, count = [], nums[0], 0
        while count < len(nums) - 1:
            if nums[count] + 1 != nums[count + 1]:
                ans.append(str(start) if start == nums[count] else f"{start}->{nums[count]}")
                start = nums[count + 1]
            count += 1
        return ans

# Reference: https://leetcode.com/problems/summary-ranges/discuss/63193/6-lines-in-Python
#======== <Solution 2> ========#
        ranges = []
        for n in nums:
            if not ranges or n > ranges[-1][-1] + 1:
                ranges += [],
            ranges[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

#======== <Solution 3> ========#
        ranges, r = [], []
        for n in nums:
            if n - 1 not in r:
                r = []
                ranges += r,
            r[1:] = n,
        return ['->'.join(map(str, r)) for r in ranges]

# Reference: https://leetcode.com/problems/summary-ranges/discuss/63474/Idea-%2B-1-Liner%3A-Group-by-number-index
#======== <Solution 4> ========#
        import itertools, operator
        ans = []
        for _, group in itertools.groupby(enumerate(nums), lambda enum: enum[1] - enum[0]):
            group = list(map(operator.itemgetter(1), group))
            ans.append(str(group[0]) if len(group) == 1 else f'{group[0]}->{group[-1]}')
        return ans

#======== <Solution 5> ========#
        from collections import defaultdict
        ranges = defaultdict(list)
        for i, n in enumerate(nums):
            ranges[n - i][1:] = n,
        return ['->'.join(map(str, r)) for r in sorted(ranges.values())]
