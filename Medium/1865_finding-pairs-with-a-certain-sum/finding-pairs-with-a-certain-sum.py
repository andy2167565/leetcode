import collections
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = collections.Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq[self.nums2[index]] -= 1  # Remove old number
        self.nums2[index] += val
        self.freq[self.nums2[index]] += 1  # Count new number

    def count(self, tot: int) -> int:
        return sum(self.freq[tot - num] for num in self.nums1)  # Traverse elements in nums1 since nums1.length <= 1000 and count function can be called at most 1000 times


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
