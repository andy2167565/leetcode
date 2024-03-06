class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Reference: https://leetcode.com/problems/minimum-cost-to-convert-string-i/solutions/4449631/c-java-python-javascript-easiest-approach-explained/
        cost_matrix = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            cost_matrix[i][i] = 0
        for x, y, z in zip(original, changed, cost):
            cost_matrix[ord(x) - ord('a')][ord(y) - ord('a')] = min(cost_matrix[ord(x) - ord('a')][ord(y) - ord('a')], z)
        for k in range(26):  # Floyd-Warshall Algorithm
            for i in range(26):
                for j in range(26):
                    cost_matrix[i][j] = min(cost_matrix[i][j], cost_matrix[i][k] + cost_matrix[k][j])
        ans = 0
        for s, t in zip(source, target):
            ans += cost_matrix[ord(s) - ord('a')][ord(t) - ord('a')]
            if ans == float('inf'):
                return -1
        return ans
