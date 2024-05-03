class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        import collections, itertools, math
        counter = collections.Counter(nums)
        squares = collections.defaultdict(set)
        for i, j in itertools.product(counter, repeat=2):
            if math.isqrt(i + j)**2 == i + j:  # (i + j) is a perfect square
                squares[i].add(j)

        def dfs(i, remain=len(nums) - 1):
            counter[i] -= 1
            arrays = sum(dfs(j, remain - 1) for j in squares[i] if counter[j]) if remain else 1
            counter[i] += 1  # Backtracking
            return arrays

        return sum(map(dfs, counter))
