class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        if not nums: return 0
        nums = sorted(set(nums))
        prev = nums[0]
        count = ans = 1
        for num in nums[1:]:
            if num == prev + 1:  # num is in the sequence
                count += 1
            else:  # num is the start of a sequence
                count = 1
            ans = max(ans, count)
            prev = num
        return ans

#======== <Solution 2> ========#
        nums, ans = set(nums), 0
        @cache
        def dp(num):
            return dp(num + 1) + 1 if num in nums else 0
        for num in nums:
            ans = max(ans, dp(num))
        return ans

#======== <Solution 3> ========#
        nums, ans = set(nums), 0
        for num in nums:
            if num - 1 not in nums:  # num is the start of a sequence
                count = 1
                while num + count in nums:  # Test (num + 1, num + 2, num + 3, ...) and stop at the first (num + count) not in the set
                    count += 1
                ans = max(ans, count)
        return ans

#======== <Solution 4> ========#
        nums, ans = set(nums), 0
        while nums:
            start = end = nums.pop()  # Set start and end of a sequence
            while start - 1 in nums:
                start -= 1
                nums.remove(start)  # Remove visited number
            while end + 1 in nums:
                end += 1
                nums.remove(end)
            ans = max(ans, end - start + 1)
        return ans
