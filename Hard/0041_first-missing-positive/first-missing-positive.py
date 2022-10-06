class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
#======== <Solution 1> ========#
        ans = 1
        for num in sorted(nums):
            if num == ans:
                ans += 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
        nums.append(0)
        n = len(nums)
        for i in range(n):  # Delete those useless elements
            if nums[i] < 0 or nums[i] > n - 1:
                nums[i] = 0
        for i in range(n):  # Use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        for i in range(1, n):
            if nums[i] < n:
                return i
        return n

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/first-missing-positive/discuss/17168/A-very-nice-solution-(from-Ants-Aasma-%40stackoverflow)
        for i in range(len(nums)):
            while 0 < nums[i] < len(nums) and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
