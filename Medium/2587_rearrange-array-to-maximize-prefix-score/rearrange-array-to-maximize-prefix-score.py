class Solution:
    def maxScore(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        nums.sort(reverse=True)
        prefix = [0]
        for num in nums:
            curr_prefix = prefix[-1] + num
            if curr_prefix <= 0:
                break
            prefix.append(curr_prefix)
        return len(prefix) - 1

#======== <Solution 2> ========#
        nums.sort()
        ans = prefix = 0
        while nums:
            prefix += nums.pop()
            if prefix <= 0:
                break
            ans += 1
        return ans

#======== <Solution 3> ========#
        import itertools
        nums.sort(reverse=True)
        return sum(num > 0 for num in itertools.accumulate(nums))
