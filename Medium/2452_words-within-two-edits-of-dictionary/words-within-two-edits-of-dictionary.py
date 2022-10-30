class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            if any(sum(c1 != c2 for c1, c2 in zip(q, d)) < 3 for d in dictionary):
                ans.append(q)
        return ans
