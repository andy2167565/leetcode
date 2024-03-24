class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # Reference: https://leetcode.com/problems/binary-trees-with-factors/solutions/125794/c-java-python-dp-solution/
        dp = {}  # dp[i]: The number of trees with i as root
        for node in sorted(arr):
            dp[node] = sum(dp[leaf] * dp.get(node // leaf, 0) for leaf in dp if not node % leaf) + 1  # All nodes can be counted as one tree in its own
        return sum(dp.values()) % (10**9 + 7)
