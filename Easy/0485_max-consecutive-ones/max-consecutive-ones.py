class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        start, ans = 0, 0
        for i in range(len(nums)):
            if not nums[i]:
                ans = max(ans, i - start)
                start = i + 1
        return max(ans, len(nums) - start)

#======== <Solution 2> ========#
        count, ans = 0, 0
        for num in nums:
            if not num:
                ans = max(ans, count)
                count = 0
            else:
                count += 1
        return max(ans, count)

#======== <Solution 3> ========#
        count, ans = 0, 0
        for num in nums:
            count = count * num + num
            ans = max(ans, count)
        return ans

#======== <Solution 4> ========#
        for i in range(1, len(nums)):
            if nums[i]:
                nums[i] += nums[i - 1]
        return max(nums)

#======== <Solution 5> ========#
        import itertools
        return max(itertools.accumulate(nums, func=lambda i, j: j and i + 1))

#======== <Solution 6> ========#
        import itertools
        return max((sum(g[1]) for g in itertools.groupby(nums) if g[0]), default=0)

#======== <Solution 7> ========#
        return len(max(''.join(map(str, nums)).split('0'), key=len))
