class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (min(arr) + max(arr)) * (len(arr) + 1) // 2 - sum(arr)
