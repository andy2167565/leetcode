class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        import collections
        counter = collections.Counter(arr)
        return any(2 * num in counter and num for num in arr) or counter[0] > 1
