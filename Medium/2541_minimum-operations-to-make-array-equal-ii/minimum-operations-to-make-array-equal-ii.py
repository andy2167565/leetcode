class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if not k: return (nums1 == nums2) - 1
        operations = balance = 0
        for num1, num2 in zip(nums1, nums2):
            diff = num1 - num2
            q, r = divmod(diff, k)
            if r:
                return -1
            if diff > 0:
                operations += q
            balance += diff
        return operations if not balance else -1
