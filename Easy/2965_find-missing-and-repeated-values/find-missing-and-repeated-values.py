class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        import collections
        counter = collections.Counter(num for row in grid for num in row)
        for i in range(1, len(grid)**2 + 1):
            if i not in counter:
                return max(counter, key=counter.get), i
