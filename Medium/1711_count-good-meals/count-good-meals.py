class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        import collections
        ans, counter = 0, collections.Counter()
        for d in deliciousness:
            for i in range(22):
                ans += counter[(1 << i) - d]
            counter[d] += 1
        return ans % (10**9 + 7)
