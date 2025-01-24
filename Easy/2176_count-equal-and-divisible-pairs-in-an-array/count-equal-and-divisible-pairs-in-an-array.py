class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        return sum(nums[i] == nums[j] and not (i * j) % k for i in range(len(nums)) for j in range(i + 1, len(nums)))
