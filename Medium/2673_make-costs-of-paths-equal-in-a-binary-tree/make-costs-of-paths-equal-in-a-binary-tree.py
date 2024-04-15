class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        # Reference: https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/solutions/3494915/java-c-python-bottom-up-and-follow-up/
        ans = 0
        for i in range(n // 2 - 1, -1, -1):
            l, r = 2 * i + 1, 2 * i + 2
            ans += abs(cost[l] - cost[r])  # The smaller child needs to catch up with the bigger child
            cost[i] += max(cost[l], cost[r])  # cost[i]: minimum cost from node i to any leaf
        return ans
