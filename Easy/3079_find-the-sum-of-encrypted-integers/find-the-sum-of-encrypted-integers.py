class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        return sum(int(max(num) * len(num)) for num in map(str, nums))
