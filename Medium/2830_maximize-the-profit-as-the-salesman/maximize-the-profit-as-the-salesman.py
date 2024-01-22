class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/maximize-the-profit-as-the-salesman/solutions/3934188/java-c-python-dp-o-n-m/
        import collections
        hashmap, dp = collections.defaultdict(list), [0] * (n + 1)  # dp[i]: The maximum golds for first i houses
        for start, end, gold in offers:
            hashmap[end].append([start, gold])
        for end in range(1, n + 1):
            dp[end] = dp[end - 1]
            for start, gold in hashmap[end - 1]:
                dp[end] = max(dp[end], dp[start] + gold)
        return dp[-1]
