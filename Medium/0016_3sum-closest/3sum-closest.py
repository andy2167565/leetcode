class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = sum(nums[:3])
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:  # Skip the duplicates
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = sum((nums[i], nums[l], nums[r]))
                if s == target:
                    return s
                if abs(s - target) < abs(ans - target):
                    ans = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return ans
