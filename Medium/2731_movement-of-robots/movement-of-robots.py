class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
#======== <Solution 1> ========#
        for i in range(len(s)):  # Two robots just pass through each other when they collide
            if s[i] == 'L':
                nums[i] -= d
            else:
                nums[i] += d
        ans = prefix = 0
        mod = 10**9 + 7
        nums.sort()
        for i in range(len(nums)):
            ans += (nums[i] * i - prefix) % mod  # Calculate the distance between robot i and all robots to its left
            prefix += nums[i] % mod
        return ans % mod

# Reference: https://leetcode.com/problems/movement-of-robots/solutions/3629710/java-c-python-ants-trick/
#======== <Solution 2> ========#
        nums = sorted(nums[i] + (d if s[i] == 'R' else -d) for i in range(len(nums)))
        return sum((i * 2 + 1 - len(nums)) * num for i, num in enumerate(nums)) % (10**9 + 7)
