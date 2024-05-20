class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # Reference: https://leetcode.com/problems/cycle-length-queries-in-a-tree/solutions/2923489/java-c-python-lowest-common-ancestor/
        ans = []
        for a, b in queries:
            ans.append(1)
            while a != b:  # Find the parents of a and b until we meet their Lowest Common Ancestor
                a, b = min(a, b), max(a, b) // 2
                ans[-1] += 1
        return ans
