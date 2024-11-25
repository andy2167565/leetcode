class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        import collections
        ans, counter = [], collections.Counter(arr1)
        for num in arr2:
            ans += [num] * counter.pop(num)
        return ans + sorted(counter.elements())
