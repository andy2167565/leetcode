class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        import itertools
        return sum(not num1 % (num2 * k) for num1, num2 in itertools.product(nums1, nums2))
