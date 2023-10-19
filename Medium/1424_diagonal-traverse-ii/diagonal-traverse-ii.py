class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        import collections
        hashmap = collections.defaultdict(list)
        for i, row in enumerate(nums):
            for j, num in enumerate(row):
                hashmap[i + j].append(num)
        return [num for k, v in hashmap.items() for num in reversed(v)]
