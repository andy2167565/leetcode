class Solution:
    def findLucky(self, arr: List[int]) -> int:
        import collections
        return max([num for num, count in collections.Counter(arr).items() if num == count] + [-1])
