class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
#======== <Solution 1> ========#
        return [len(set(nums[:i + 1])) - len(set(nums[i + 1:])) for i in range(len(nums))]

#======== <Solution 2> ========#
        import collections
        ans, prefix, suffix = [], collections.defaultdict(int), collections.Counter(nums)
        for num in nums:
            prefix[num] += 1
            suffix[num] -= 1
            if not suffix[num]:
                suffix.pop(num)
            ans.append(len(prefix) - len(suffix))
        return ans
