# Reference: https://leetcode.com/problems/smallest-string-with-swaps/solutions/387524/short-python-union-find-solution-w-explanation/
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        import collections
        uf, children = UnionFind(len(s)), collections.defaultdict(list)
        for a, b in pairs:
            uf.union(a, b)
        for i, c in enumerate(s):
            children[uf.find(i)].append(c)
        for i in children.keys():
            children[i].sort(reverse=True)
        return ''.join(children[uf.find(i)].pop() for i in range(len(s)))
